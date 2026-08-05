from audio_capture import record_audio
from classifier import AudioClassifier
from threat_assessment import ThreatAssessment
from decision_engine import DecisionEngine
from evidence import EvidenceManager
from alerts import AlertManager

import os
# import config


# -------------------------
# Initialize all modules
# -------------------------

classifier = AudioClassifier()

threatAssessment = ThreatAssessment()

decisionEngine = DecisionEngine()

evidenceManager = EvidenceManager()

alertManager = AlertManager()


print("Monitoring started...")


try:

    while True:

        # -------------------------
        # Record audio
        # -------------------------

        waveform, audio_path = record_audio()

        # -------------------------
        # Classify audio
        # -------------------------

        predictions = classifier.predict(
            waveform
        )

        print("\nTop Predictions\n")

        for prediction in predictions:

            print(

                f"{prediction['label']:<25}"

                f"{prediction['confidence']:.3f}"

            )

        # -------------------------
        # Threat Assessment
        # -------------------------

        assessment = threatAssessment.assess(
            predictions
        )

        # -------------------------
        # Decision Making
        # -------------------------

        decision = decisionEngine.decide(
            assessment
        )

        # -------------------------
        # Debug Output
        # -------------------------

        print("\nAssessment")

        print(assessment)

        print("\nDecision")

        print(decision)

        # -------------------------
        # Save Evidence
        # -------------------------

        if decision["save_evidence"]:

            evidenceManager.save(
                assessment,
                audio_path
            )

        # -------------------------
        # Send Alert
        # -------------------------

        if decision["send_alert"]:

            alertManager.send_alert(
                assessment
            )

        # -------------------------
        # No Threat
        # -------------------------

        if (
            not decision["save_evidence"]
            and
            not decision["send_alert"]
        ):

            print("No threat detected.")

        # -------------------------
        # Delete temporary recording
        # -------------------------

        if os.path.exists(audio_path):

            os.remove(audio_path)

except KeyboardInterrupt:

    print("\nMonitoring stopped by user.")