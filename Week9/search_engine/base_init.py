from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship


Base = declarative_base()


# class Website(Base):
#     __tablename__ = "website"
#     id = Column(Integer, primary_key = True)
#     url = Column(String)
#     title = Column(String)
#     domain = Column(String)
#     pages_count = Column(Integer)
#     HTML_ver = Column(Float)


class Page(Base):
    __tablename__ = "table"
    id = Column(Integer, primary_key=True)
    website = Column(String)
    url = Column(String)
    title = Column(String)
    description = Column(String)
    ads = Column(Integer)
    SSL = Column(bool)
    multi_lang = Column(Integer)
