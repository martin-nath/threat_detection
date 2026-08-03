import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def preprocess(audio_file):
    y, sr = librosa.load(audio_file, sr=None)

    print("Waveform shape: ", y.shape)
    print("Sample Rate: ", sr)

    mel_spec = librosa.feature.melspectrogram(
        y = y,
        sr = sr
    )

    mel_spec_db = librosa.power_to_db(
        mel_spec,
        ref=np.max
    )

    plt.figure(figsize=(10, 4))

    librosa.display.specshow(
        mel_spec_db,
        sr=sr,
        x_axis='time',
        y_axis='mel'
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title("Mel Spectrogram")

    plt.savefig("mel_spectrogram.png")
    plt.close()

    return "mel_spectrogram.png"