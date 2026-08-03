from audio_capture import record_audio
from classifier import AudioClassifier
from decision_engine import DecisionEngine
from evidence import EvidenceManager
from alerts import AlertManager
import os
import config

classifier = AudioClassifier()
decisionEngine = DecisionEngine()
evidenceManager = EvidenceManager()
alertManager = AlertManager()

waveform, audio_path = record_audio()

predictions = classifier.predict(
    waveform
)

print("\nTop Predictions\n")

for prediction in predictions:
    print(
        f"{prediction['label']:<25}"
        f"{prediction['confidence']:.3f}"
    )

decision = decisionEngine.evaluate(predictions)
print()
print(decision)

if decision['threat']:
    evidenceManager.save(decision, audio_path)

    alertManager.send_alert(decision)
else:
    print("No threat detected")

if os.path.exists(audio_path):
    os.remove(config.OUTPUT_AUDIO)