import config

class ConfidenceFilter:
    def __init__(self):
        print("Initializing confidence filter")

    def filter(self, predictions):
        accepted_predictions = []
        rejected_predictions = []

        for prediction in predictions:
            label = prediction['label']
            confidence = prediction['confidence']

            threshold = config.CONFIDENCE_OVERRIDES.get(
                label,
                config.DEFAULT_CONFIDENCE_THRESHOLD
            )

            if confidence >= threshold:
                accepted_predictions.append({
                    "label": label,
                    "confidence": confidence,
                    "threshold": threshold
                })
            else:
                rejected_predictions.append({
                    "label": label,
                    "confidence": confidence,
                    "threshold": threshold
                })

        print("Confidence Filter Summary")
        print(f"Total Predictions: {len(predictions)}")
        print(f"Accepted: {len(accepted_predictions)}")
        print(f"Rejected: {len(rejected_predictions)}")

        return accepted_predictions, rejected_predictions