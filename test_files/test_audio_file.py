from classifier import AudioClassifier
import librosa

classifier = AudioClassifier()

for i in range(1, 4):

    audio_file = f"./test_sounds/gunfire_{i}.mp3"

    waveform, sr = librosa.load(
        audio_file,
        sr=32000,
        mono=True
    )

    predictions = classifier.predict(waveform)

    print("\nPredictions\n")

    for prediction in predictions:
        print(
            f"{prediction['label']:<30}"
            f"{prediction['confidence']:.3f}"
        )