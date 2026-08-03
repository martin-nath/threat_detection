import sounddevice as sd
import soundfile as sf

from config import (
    AUDIO_SAMPLE_RATE,
    CHANNELS,
    RECORD_SECONDS,
    OUTPUT_AUDIO
)


def record_audio():

    print("Recording started...")

    audio = sd.rec(
        int(RECORD_SECONDS * AUDIO_SAMPLE_RATE),
        samplerate=AUDIO_SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32"
    )

    sd.wait()

    sf.write(
        OUTPUT_AUDIO,
        audio,
        AUDIO_SAMPLE_RATE
    )

    print("Recording completed.")

    return audio.squeeze(), OUTPUT_AUDIO