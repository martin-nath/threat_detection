# AI Audio Threat Detection System

## Overview

The AI Audio Threat Detection System is an intelligent surveillance prototype that continuously monitors ambient audio, classifies acoustic events using a pretrained CNN14 deep learning model, assesses the severity of detected events, and automatically takes appropriate actions such as saving evidence and sending email alerts.

This project was developed as part of an internship to demonstrate how artificial intelligence can assist in the early detection of potentially dangerous situations through audio analysis.

## Features

- Continuous microphone audio monitoring
- Audio classification using pretrained CNN14
- Rule-based threat assessment engine
- Priority-based decision making
- Automatic evidence storage
- Email alert notifications
- Modular architecture for future expansion

## System Architecture

```text
                +------------------+
                |  Microphone      |
                +--------+---------+
                         |
                         v
                +------------------+
                | Audio Capture    |
                +--------+---------+
                         |
                         v
                +------------------+
                | CNN14 Classifier |
                +--------+---------+
                         |
                         v
                +----------------------+
                | Threat Assessment    |
                +--------+-------------+
                         |
                         v
                +----------------------+
                | Decision Engine      |
                +--------+-------------+
                         |
              +----------+----------+
              |                     |
              v                     v
     +----------------+     +----------------+
     | Evidence       |     | Email Alerts   |
     | Manager        |     |                |
     +----------------+     +----------------+
```

## Project Structure

```text
audio_project/
│
├── alerts.py
├── audio_capture.py
├── classifier.py
├── config.py
├── decision_engine.py
├── evidence.py
├── main.py
├── preprocessing.py
├── threat_assessment.py
├── requirements.txt
├── README.md
│
├── models/
│   └── panns/
│       ├── models.py
│       ├── pytorch_utils.py
│       └── class_labels_indices.csv
│
├── recordings/
└── evidence/
```

## Technologies Used

- Python
- PyTorch
- CNN14 (PANNs)
- NumPy
- Librosa
- SoundDevice
- SoundFile
- SMTP (Email Alerts)

## Installation

1. Clone the repository.

```bash
git clone https://github.com/martin-nath/threat_detection.git
cd audio_project
```

2. Create a virtual environment.

```bash
python -m venv .venv
```

3. Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

4. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Configuration

Before running the project, update the required settings in `config.py`.

Configure the following:

- Audio recording duration
- Audio sample rate
- Email sender address
- Email receiver address
- SMTP server
- SMTP port
- Email password

Make sure your microphone is connected and accessible to the application.

## Pretrained Model

This project uses the pretrained **CNN14** model from the **PANNs (Pretrained Audio Neural Networks)** project.

The pretrained weights are **not included** in this repository because the model file size exceeds GitHub's maximum file size limit.

Download the pretrained model from the official PANNs release:

https://zenodo.org/records/3987831

Download the following file:

```
Cnn14_mAP=0.431.pth
```

After downloading, place it inside:

```
models/
└── panns/
    └── Cnn14_mAP=0.431.pth
```

## How to Run

Run the application using:

```bash
python main.py
```

The system will:

1. Record audio from the microphone.
2. Classify the recorded audio using CNN14.
3. Assess the detected audio events.
4. Decide whether any action is required.
5. Save evidence for significant threats.
6. Send an email alert for high-priority threats.
```

## Current Limitations

- Supports only audio-based threat detection.
- Uses a rule-based threat assessment engine.
- Does not perform speech recognition.
- Does not support video analysis.
- Designed as an internship prototype and not for production deployment.

## Future Enhancements

Planned improvements include:

- Confidence-weighted threat assessment
- Continuous audio monitoring using a circular buffer
- Speech recognition using Whisper
- Keyword-based emergency detection
- YOLO-based visual threat detection
- Multi-modal threat assessment (audio + video)
- SMS and mobile notifications
- Real-time monitoring dashboard

## Acknowledgements

This project uses the following open-source resources:

- **PANNs (Pretrained Audio Neural Networks)** for the CNN14 pretrained model.
- **PyTorch** for the deep learning framework.
- **Librosa** for audio processing.
- **SoundDevice** for microphone input.