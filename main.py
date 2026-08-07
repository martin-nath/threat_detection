from audio_capture import record_audio
from classifier import AudioClassifier
from threat_assessment import ThreatAssessment
from decision_engine import DecisionEngine
from evidence import EvidenceManager
from alerts import AlertManager
from confidence_filter import ConfidenceFilter
from display import (
    display_assessment,
    display_decision
)
from monitor import ContinuousMonitor

import os



classifier = AudioClassifier()
confidenceFilter = ConfidenceFilter()
continuousMonitor = ContinuousMonitor()
threatAssessment = ThreatAssessment()
decisionEngine = DecisionEngine()
evidenceManager = EvidenceManager()
alertManager = AlertManager()

print("Monitoring started...")


try:

    while True:


        waveform, audio_path = record_audio()


        predictions = classifier.predict(waveform)

        accepted_predictions, rejected_predictions = (confidenceFilter.filter(predictions))
        continuousMonitor.update(accepted_predictions)
        monitor_state = continuousMonitor.get_state()

        print("\nMonitor State: ")

        if monitor_state:
            for label, count in monitor_state.items():
                print(f"{label:<25}{count}")
        else:
                print("No events recorded.")

        assessment = threatAssessment.assess(accepted_predictions)

        print("\nTop Predictions\n")
        
        for prediction in predictions:
            print(
        f"{prediction['label']:<25}"
        f"{prediction['confidence']:.3f}"
            )

        decision = decisionEngine.decide(
            assessment
        )
        
        display_assessment(assessment)
        display_decision(decision)

        print("\nReasons:")

        if assessment["reasons"]:
            for reason in assessment["reasons"]:
                print(f"- {reason}")
        else:
            print("None")


        if decision["save_evidence"]:

            evidenceManager.save(
                assessment,
                audio_path
            )


        if decision["send_alert"]:

            alertManager.send_alert(
                assessment
            )
        

        if os.path.exists(audio_path):

            os.remove(audio_path)

except KeyboardInterrupt:

    print("\nMonitoring stopped by user.")