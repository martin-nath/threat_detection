import config


class ContinuousMonitor:

    def __init__(self):
        print("Initializing Continuous Monitor...")
        self.event_counts = {}

    def update(self, accepted_predictions):

        current_labels = set()

        for prediction in accepted_predictions:

            label = prediction["label"]

            if label not in (
                "Speech",
                "Scream",
                "Screaming",
                "Glass",
                "Gunshot, gunfire",
                "Explosion"
            ):
                continue

            current_labels.add(label)

            if label not in self.event_counts:
                self.event_counts[label] = 0

            self.event_counts[label] += 1

        # Reset events that disappeared

        for label in list(self.event_counts.keys()):

            if label not in current_labels:
                self.event_counts[label] = max(0, self.event_counts[label] - 1)

    def get_state(self):
        return self.event_counts

    def get_threat_signals(self):

        signals = []

        if self.event_counts.get("Gunshot, gunfire", 0) >= 1:
            signals.append("Weapon Activity")

        if self.event_counts.get("Explosion", 0) >= 1:
            signals.append("Explosion Activity")

        scream_count = (
            self.event_counts.get("Scream", 0)
            +
            self.event_counts.get("Screaming", 0)
        )

        if (
            scream_count >= 1
            and
            self.event_counts.get("Glass", 0) >= 1
        ):
            signals.append("Possible Assault")

        return signals

    def get_continuous_events(self):

        continuous_events = []

        for label, count in self.event_counts.items():

            threshold = config.CONTINUOUS_THRESHOLDS.get(
                label,
                999
            )

            if count >= threshold:

                continuous_events.append({
                    "label": label,
                    "count": count
                })

        return continuous_events