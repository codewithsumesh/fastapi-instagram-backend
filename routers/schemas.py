from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str

class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: str

#for PostDisplay
class User(BaseModel):     
    username: str

#for PostDisplay     
class Comment(BaseModel):
    id:int
    text:str
    username:str       # comment can be created by other users
    timestamp: datetime

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type:str
    caption:str
    timestamp:datetime
    user : User   
    comments:List[Comment]
'''
  {
    "id": 1,
    "image_url": "images/cat_OOoRhi.jpg",
    "image_url_type": "relative",
    "caption": "me perfect creature",
    "timestamp": "2026-07-04T19:19:40.091655",
    "user": {
      "username": "nava"
    },
    "comments": [
      {
        "text": "hahaha",
        "username": "hahaha",
        "timestamp": "2026-07-04T19:20:44.613637"
      }
'''

class UserAuth(BaseModel):
    id : int
    username:str
    email:str

class CommentBase(BaseModel):
    username:str
    text: str
    post_id: int