from sqlalchemy import create_engine
from receiver import Base

engine = create_engine('sqlite:///mail_receiver.db', echo=True)

Base.metadata.create_all(engine)
