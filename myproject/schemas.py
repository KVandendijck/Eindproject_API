from pydantic import BaseModel

class TweetsBase(BaseModel):
    pass


class TweetsCreate(TweetsBase):
    pass


class Tweets(TweetsBase):
    id: int
    message_id: int
    profile_id: int
    text: str

    class Config:
        orm_mode = True

class SearchBase(BaseModel):
    name: str


class SearchCreate(SearchBase):
    pass


class Search(SearchBase):
    id: int
    profile_id: str
    time: str
    amount: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True