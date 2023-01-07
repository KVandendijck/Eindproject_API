from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas
import requests
import auth


def search_user(db: Session, item: schemas.SearchCreate):
    headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAEyujQEAAAAAJ0Pcc2iUwHFq3tE5QXmkGZpM3qs%3Ddp0Tq4kSkqMeXGF8lNENr9apXGa6Mf6BGdAMLbajecB0EtIBXE"}
    r = requests.get("https://api.twitter.com/2/users/by/username/" + item.name, headers=headers)
    data = r.json()
    #amount of tweets
    y = requests.get("https://api.twitter.com/2/users/" + data["data"]["id"] + "?user.fields=public_metrics",headers=headers)
    tweet_amount = y.json()["data"]["public_metrics"]["tweet_count"]
    #create database entry
    # get all tweets and put them in database
    k = requests.get("https://api.twitter.com/2/users/" + data["data"]["id"] + "/tweets?max_results=5", headers=headers)
    data2 = k.json()
    for i in data2["data"]:
        if not db.query(models.Tweets).filter(models.Tweets.message_id == i["id"]).first():
            db_tweet = models.Tweets(message_id=i["id"], profile_id=data["data"]["id"], text=i["text"])
            db.add(db_tweet)
            db.commit()
            db.refresh(db_tweet)
    db_search = models.Searches(name=data["data"]["name"], profile_id=data["data"]["id"], time=datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"), amount=tweet_amount)
    db.add(db_search)
    db.commit()
    db.refresh(db_search)
    return db_search


def get_all_tweet(db: Session):
    return db.query(models.Tweets).all()

def get_all_searches(db: Session):
    return db.query(models.Searches).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_all_users(db: Session):
    return db.query(models.User).all()


def edit_username(db: Session, user = schemas.UserBase, id = int):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    db_user.username = user.username
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, id = int):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    db.delete(db_user)
    db.commit()
    return {"detail": "User is deleted"}
