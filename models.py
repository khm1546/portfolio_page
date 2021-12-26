from sqlalchemy import Column, Integer, String
from database import Base


class Members(Base):

    __tablename__ = 'yujin'

    idx = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(30, 'utf8mb4_unicode_ci'))

    def __init__(self, name, type, question):
        self.name = name
        self.type = type
        self.question = question

