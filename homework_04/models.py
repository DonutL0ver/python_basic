
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from homework_04.main import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    user = relationship("User", back_populates="posts")

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
