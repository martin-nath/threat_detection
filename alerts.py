import smtplib
from email.message import EmailMessage

import config


class AlertManager:

    def send_alert(self, decision):

        message = EmailMessage()

        message["Subject"] = "Threat Detected"
        message["From"] = config.EMAIL_SENDER
        message["To"] = config.EMAIL_RECEIVER

        message.set_content(
            f"""Threat Detected

Label      : {decision["label"]}

Confidence : {decision["confidence"]:.2f}

Threshold  : {decision["threshold"]:.2f}

Time       : {decision["timestamp"]}

Message    : {decision["message"]}
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
            print(f"Failed to send alert email.\n{error}")