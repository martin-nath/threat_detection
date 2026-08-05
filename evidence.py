from pathlib import Path
import shutil
import json

import config


class EvidenceManager:

    def save(self, assessment, audio_path):

        # Convert timestamp into a Windows-safe folder name
        timestamp = (
            assessment["timestamp"]
            .replace(":", "-")
            .replace(".", "-")
        )

        # Create incident folder
        incident_folder = (
            Path(config.EVIDENCE_FOLDER)
            / timestamp
        )

        incident_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        # Copy recorded audio
        destination = (
            incident_folder
            / "audio.wav"
        )

        shutil.copy(
            audio_path,
            destination
        )

        # Metadata to be saved
        metadata = {

            "timestamp": assessment["timestamp"],

            "priority": assessment["priority"],

            "score": assessment["score"],

            "categories": assessment["categories"],

            "events": assessment["events"]

        }

        # metadata.json path
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
            f"Evidence saved successfully at:\n{incident_folder}"
        )