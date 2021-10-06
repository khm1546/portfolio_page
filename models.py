from sqlalchemy import Column, Integer, String
from database import Base


class Members(Base):

    __tablename__ = 'cs'

    idx = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20, 'utf8mb4_unicode_ci'))
    type = Column(String(10))
    question = Column(String(10))

    def __init__(self, name, type, question):
        self.name = name
        self.type = type
        self.question = question

