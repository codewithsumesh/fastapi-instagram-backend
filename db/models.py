from .database import Base
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbPost',back_populates='user')

class DbPost(Base):
    __tablename__ = 'post'
    id =Column(Integer,primary_key=True,index=True)
    image_url = Column(String)
    image_url_type= Column(String)
    caption = Column(String)
    timestamp= Column(DateTime)
    user_id= Column(Integer,ForeignKey('user.id'))
    user = relationship('DbUser',back_populates='items')  # for use of minimal Queries
    comments = relationship('DbComment',back_populates='post')

class DbComment(Base):
    __tablename__= 'comment'
    id=Column(Integer,primary_key=True,index=True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime)
    post_id= Column(Integer,ForeignKey('post.id'))
    post= relationship('DbPost',back_populates='comments')

    '''
    ForeignKey = stores the ID in the database.
relationship() = lets Python navigate between objects.
back_populates = links the two relationships so you can move both directions:
post.user ➜ the owner of the post.
user.items ➜ all posts created by that user.
when post create
 │
 ├── id = 101
 ├── caption = "Hello"
 ├── user_id = 1
 │
 └── user ─────────► DbUser (we get user info)
                     │
                     ├── id = 1
                     └── username = "nava"
                     "Give me the User object that owns this post."
It does not return the user_id; it returns the entire DbUser object associated with that post.
    '''
