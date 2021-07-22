import config
from sqlalchemy.sql import ClauseElement
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()


class Sentence(Base):
    __tablename__ = 'sentence'
    id = Column(Integer, primary_key=True)
    source_text = Column(String)
    case = Column(String)
    number = Column(String)
    gender = Column(String)
    result = Column(String)
    create_datetime = Column(DateTime, default=datetime.now())


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        instance = model(**params)
        session.add(instance)
        session.flush()
        return instance, True


def get(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        return None


def drop_tables():
    Base.metadata.drop_all(config.ENGINE)


def create_tables():
    Base.metadata.create_all(config.ENGINE)


if __name__ == '__main__':
    create_tables()
