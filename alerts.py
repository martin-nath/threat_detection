import smtplib
from email.message import EmailMessage

import config


class AlertManager:

    def send_alert(self, assessment):

        message = EmailMessage()

        message["Subject"] = "Threat Detected"
        message["From"] = config.EMAIL_SENDER
        message["To"] = config.EMAIL_RECEIVER

        message.set_content(
f"""Threat Detected

Time       : {assessment["timestamp"]}

Priority   : {assessment["priority"]}

Score      : {assessment["score"]}

Categories : {", ".join(assessment["categories"])}

Detected Events:

{self.format_events(assessment["events"])}
"""
        )

        try:

            with smtplib.SMTP(
                config.SMTP_SERVER,
                config.SMTP_PORT,
            ) as server:

                server.starttls()

                server.login(
                    config.EMAIL_SENDER,
                    config.EMAIL_PASSWORD,
                )

                server.send_message(message)

            print("Alert email sent successfully.")

        except Exception as error:

            print(
                f"Failed to send alert email.\n{error}"
            )

    def format_events(self, events):

        text = ""

        for event in events:

            text += (
                f"- {event['label']} "
                f"(Confidence: {event['confidence']:.2f})\n"
            )

        return text