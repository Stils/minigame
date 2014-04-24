from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(120), unique=True)
    x = Column(Integer)
    y = Column(Integer)

    def __init__(self, name=None, password=None):
        self.name = name
        self.x = 0
        self.password = password
        self.y = 0

    def __repr__(self):
        return '<User %r>' % (self.name)
