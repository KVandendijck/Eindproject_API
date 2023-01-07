from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Searches(Base):
    __tablename__ = "searches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    profile_id = Column(Integer)
    time = Column(String)
    amount = Column(Integer, index=True)
    tweets = relationship("Tweets", back_populates="searches")


class Tweets(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer)
    profile_id = Column(Integer, ForeignKey("searches.profile_id"))
    text = Column(String)
    searches = relationship("Searches", back_populates="tweets")
