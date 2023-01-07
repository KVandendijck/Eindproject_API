from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
import auth
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/profile")
def create_search_for_user(item: schemas.SearchCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.search_user(db=db, item=item)


@app.get("/alltweets")
def get_tweets(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.get_all_tweet(db=db)

@app.get("/allsearches")
def get_tweets(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.get_all_searches(db=db)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/allusers", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.get_all_users(db=db)


@app.put("/users/{id}", response_model=schemas.User)
def edit_username(id: int, user: schemas.UserBase, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.edit_username(db, user, id=id)

@app.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.delete_user(db, id=id)
