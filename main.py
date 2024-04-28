import smtplib
import os

from models.receiver import MailReceiver
from config import get_stmp_server
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv


def intialize_db() -> Session:
    engine = create_engine("sqlite:///mail_receiver.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def send_email(
    server: smtplib.SMTP, sender: str, receiver: MailReceiver, subject: str, body: str
) -> None:
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver.email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()
    server.sendmail(sender, receiver.email, text)
    server.quit()


def main():
    # Load the environment variables
    load_dotenv()

    # Get sender email from environment
    sender = os.getenv("SENDER_EMAIL")

    # Initialize the database
    session = intialize_db()

    # Get the SMTP server
    server = get_stmp_server()

    # Get all the receivers
    receivers = MailReceiver.get_all(session)

    # Send the email to all the receivers
    for receiver in receivers:
        send_email(server, sender, receiver, "Hello", "This is a test email")


if __name__ == "__main__":
    main()
