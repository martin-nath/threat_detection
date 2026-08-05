# import config
# from datetime import datetime


# class DecisionEngine:

#     def evaluate(self, predictions):

#         for prediction in predictions:

#             label = prediction["label"]
#             confidence = prediction["confidence"]

#             if label in config.THREAT_SOUNDS:

#                 threshold = config.THREAT_SOUNDS[label]

#                 if confidence >= threshold:

#                     return {
#                         "threat": True,
#                         "label": label,
#                         "confidence": confidence,
#                         "threshold": threshold,
#                         "message": f"{label} detected.",
#                         "timestamp": datetime.now().isoformat()
#                     }

#         return {
#             "threat": False,
#             "label": None,
#             "confidence": 0.0,
#             "threshold": None,
#             "message": "No threat detected.",
#             "timestamp": datetime.now().isoformat()
#         }



# from datetime import datetime

class DecisionEngine:

    def decide(self, assessment):

        priority = assessment["priority"]

        decision = {

            "save_evidence": False,

            "send_alert": False

        }

        if priority == "Ignore":
            return decision

        if priority == "Medium":
            decision["save_evidence"] = True
            return decision

        if priority in ("High", "Critical"):
            decision["save_evidence"] = True
            decision["send_alert"] = True
            return decision

        return decision