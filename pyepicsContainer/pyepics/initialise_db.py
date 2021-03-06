import os
from sqlalchemy import ARRAY, Float, Column, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.util.queue import Empty
from time import sleep

Base = declarative_base()


class CCStrace1(Base):
    __tablename__ = 'ccs_trace1'
    id = Column(Integer, primary_key=True)
    signal = Column(ARRAY(Float))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


if __name__ == "__main__":
    user = os.getenv('POSTGRES_USER')
    passwd = os.getenv('POSTGRES_PASSWORD')
    dbname = os.getenv('POSTGRES_DB')
    # host = '0.0.0.0'
    host = 'postgres'
    port = '5432'
    engine = create_engine(
            f'postgresql://{user}:{passwd}@{host}:{port}/{dbname}',
            echo=True
        )
    while True:
        try:
            print(engine)
            Base.metadata.create_all(engine)
            break
        except Empty:
            sleep(2)

