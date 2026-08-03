from models.panns.models import Cnn14
import torch
from pathlib import Path
import csv
import config

class AudioClassifier:

    def __init__(self):

        print("Creating CNN14 architecture...")

        self.model = Cnn14(
            sample_rate=config.PANNS_SAMPLE_RATE,
            window_size=config.WINDOW_SIZE,
            hop_size=config.HOP_SIZE,
            mel_bins=config.MEL_BINS,
            fmin=config.FMIN,
            fmax=config.FMAX,
            classes_num=config.CLASSES_NUM
    )

        print("CNN14 architecture created.")

        print("Loading pretrained weights...")

        checkpoint_path = checkpoint_path = config.PANNS_MODEL

        checkpoint = torch.load(
            checkpoint_path,
            map_location=torch.device("cpu")
        )

        self.model.load_state_dict(checkpoint['model'])

        print("Weights loaded successfully")

        self.model.eval()
        print("Evaluation mode enabled")

        print("Loading Audioset labels...")

        metadata_file = config.PANNS_LABELS
        self.labels = []

        with open(metadata_file, "r", encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.labels.append(row['display_name'])

        print(f"{len(self.labels)} labels loaded")

    def predict(self, waveform):

        waveform = torch.from_numpy(waveform)

        waveform = waveform.to(torch.float32)

        waveform = waveform.unsqueeze(0)

        with torch.no_grad():

            output = self.model(waveform, None)

        clipwise_output = output['clipwise_output']

        top_scores, top_indices = torch.topk(
            clipwise_output,
            k=config.TOP_K,
            dim=1
        )

        predictions = []

        for score, index in zip(top_scores[0], top_indices[0]):

            predictions.append({
                "index": index.item(),
                "label": self.labels[index.item()],
                "confidence": score.item()
            })

        return predictions