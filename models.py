from sqlalchemy import Column, Integer, String
from database import Base


class Members(Base):

    __tablename__ = 'cs'

    idx = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50, 'utf8mb4_unicode_ci'))

    def __init__(self, name):
        self.name = name

