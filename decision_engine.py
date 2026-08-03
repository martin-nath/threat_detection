import config
from datetime import datetime


class DecisionEngine:

    def evaluate(self, predictions):

        for prediction in predictions:

            label = prediction["label"]
            confidence = prediction["confidence"]

            if label in config.THREAT_SOUNDS:

                threshold = config.THREAT_SOUNDS[label]

                if confidence >= threshold:

                    return {
                        "threat": True,
                        "label": label,
                        "confidence": confidence,
                        "threshold": threshold,
                        "message": f"{label} detected.",
                        "timestamp": datetime.now().isoformat()
                    }

        return {
            "threat": False,
            "label": None,
            "confidence": 0.0,
            "threshold": None,
            "message": "No threat detected.",
            "timestamp": datetime.now().isoformat()
        }