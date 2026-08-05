from datetime import datetime

class ThreatAssessment:

    def __init__(self):

        print("Initializing Threat Assessment Engine...")

        self.threat_database = {

            "Gunshot, gunfire": {
                "category": "Weapon",
                "score": 10,
                "priority": "Critical"
            },

            "Explosion": {
                "category": "Explosion",
                "score": 10,
                "priority": "Critical"
            },

            "Scream": {
                "category": "Human Distress",
                "score": 8,
                "priority": "High"
            },

            "Glass": {
                "category": "Property Damage",
                "score": 4,
                "priority": "Medium"
            },

            "Speech": {
                "category": "Speech",
                "score": 8,
                "priority": "High"
            },

            "Silence": {
                "category": "Silence",
                "score": 10,
                "priority": "High"
            }
        }

        print(
            f"{len(self.threat_database)} threat definitions loaded."
        )

    def assess(self, predictions):

        assessment = {

            "timestamp": datetime.now().isoformat(),

            "score": 0,

            "priority": "Ignore",

            "events": [],

            "categories": []

        }

        for prediction in predictions:

            label = prediction["label"]

            confidence = prediction["confidence"]

            if label in self.threat_database:

                threat_info = self.threat_database[label]

                assessment["score"] += threat_info["score"]

                if (
                    threat_info["category"]
                    not in assessment["categories"]
                ):

                    assessment["categories"].append(
                        threat_info["category"]
                    )

                assessment["events"].append({

                    "label": label,

                    "category": threat_info["category"],

                    "score": threat_info["score"],

                    "confidence": confidence

                })

        # -------------------------
        # Priority Logic
        # -------------------------

        if "Weapon" in assessment["categories"]:

            assessment["priority"] = "Critical"

        elif "Explosion" in assessment["categories"]:

            assessment["priority"] = "Critical"

        elif (
            len(assessment["categories"]) >= 2
            and
            assessment["score"] >= 8
        ):

            assessment["priority"] = "High"

        elif "Human Distress" in assessment["categories"]:

            assessment["priority"] = "High"

        elif "Property Damage" in assessment["categories"]:

            assessment["priority"] = "Medium"

        else:

            assessment["priority"] = "Ignore"

        return assessment