import sounddevice as sd
import soundfile as sf

from config import (
    AUDIO_SAMPLE_RATE,
    CHANNELS,
    CHUNK_DURATION,
    OUTPUT_AUDIO
)


def record_audio():

    print("Recording started...")

    audio = sd.rec(
        int(CHUNK_DURATION * AUDIO_SAMPLE_RATE),
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