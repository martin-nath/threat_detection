from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ===========================
# Audio Recording
# ===========================

AUDIO_SAMPLE_RATE = 16000
CHANNELS = 1
# RECORD_SECONDS = 5
CHUNK_DURATION = 3
OUTPUT_AUDIO = "recordings/recording.wav"

# ===========================
# PANNs Model
# ===========================

PANNS_MODEL = "models/panns/Cnn14_mAP=0.431.pth"
PANNS_LABELS = "models/panns/class_labels_indices.csv"

TOP_K = 5

PANNS_SAMPLE_RATE = 32000
WINDOW_SIZE = 1024
HOP_SIZE = 320
MEL_BINS = 64
FMIN = 50
FMAX = 14000
CLASSES_NUM = 527

# ===========================
# Confidence Filter
# ===========================

DEFAULT_CONFIDENCE_THRESHOLD = 0.10 # Thresholds will be calibrated in future versions.

CONFIDENCE_OVERRIDES = {
    "Gunshot, gunfire": 0.50,
    "Explosion": 0.50,
    "Scream": 0.50
}

CONTINUOUS_THRESHOLDS = {
    "Gunshot, gunfire": 1,
    "Explosion": 1,
    "Scream": 2,
    "Screaming": 2,
    "Glass": 2,
    "Speech": 5
}

# ===========================
# Email Configuration
# ===========================

EMAIL_SENDER = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


# =============================
# Evidence
# =============================

EVIDENCE_FOLDER = "evidence"