import smtplib
from pydantic import BaseModel

class SMTPConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str


def get_stmp_server() -> smtplib.SMTP:
    config = SMTPConfig(
        host='smtp.gmail.com',
        port=587,
        username="",
        password=""
    )
    server = smtplib.SMTP(config.host, config.port)
    server.starttls()
    server.login(config.username, config.password)
    return server