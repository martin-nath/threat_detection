from pathlib import Path
import shutil
import json

import config


class EvidenceManager:

    def save(self, decision, audio_path):

        # Convert timestamp into a Windows-safe folder name
        timestamp = (
            decision["timestamp"]
            .replace(":", "-")
            .replace(".", "-")
        )

        # Create incident folder path
        incident_folder = (
            Path(config.EVIDENCE_FOLDER)
            / timestamp
        )

        # Create the folder
        incident_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        # Copy the recorded audio
        destination = (
            incident_folder
            / "audio.wav"
        )

        shutil.copy(
            audio_path,
            destination
        )

        # Create metadata dictionary
        metadata = {

            "timestamp": decision["timestamp"],

            "label": decision["label"],

            "confidence": decision["confidence"],

            "threshold": decision["threshold"],

            "message": decision["message"]

        }

        # Path for metadata.json
        metadata_path = (
            incident_folder
            / "metadata.json"
        )

        # Save metadata
        with open(
            metadata_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4
            )

        print(
            f"Evidence saved successfully at {incident_folder}"
        )