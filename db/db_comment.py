from sqlalchemy.orm import Session
from db.models import DbComment
from routers.schemas import CommentBase
from datetime import datetime

def create(db : Session ,request: CommentBase):
    new__comment = DbComment(
        username = request.username,
        text = request.text,
        post_id = request.post_id,
        timestamp = datetime.now()
    )
    db.add(new__comment)
    db.commit()
    db.refresh(new__comment)
    return new__comment

def get_all(db: Session,post_id:int):
    return db.query(DbComment).filter(DbComment.post_id ==post_id).all()
