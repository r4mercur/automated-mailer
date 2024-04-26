from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime

Base = declarative_base()

class MailReceiver(Base):
    __tablename__ = 'mail_receiver'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    last_name = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    def __init__(self, email: str, name: str, last_name: str):
        self.email = email
        self.name = name
        self.last_name = last_name

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()