import smtplib

from models.receiver import MailReceiver
from config import get_stmp_server
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


def intialize_db() -> Session:
    engine = create_engine('sqlite:///mail_receiver.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def send_email(server: smtplib.SMTP, receiver: MailReceiver, subject: str, body: str) -> None:
    message = MIMEMultipart()
    message['From'] = "<define mail from service>"
    message['To'] = receiver.email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    text = message.as_string()
    server.sendmail("<define mail from service>", receiver.email, text)
    server.quit()


def main():
    # Initialize the database
    session = intialize_db()

    # Get the SMTP server
    server = get_stmp_server()
    
    # Get all the receivers
    receivers = MailReceiver.get_all(session)

    # Send the email to all the receivers
    for receiver in receivers:
        send_email(server, receiver, "Hello", "This is a test email")

if __name__ == "__main__":
    main()