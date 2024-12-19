from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from base import Base

class User(Base):
    """ User """

    __tablename__ = "user"

    name = Column(String(50), primary_key=True)
    family = Column(Boolean, nullable=False)
    login = Column(Boolean, nullable=False)
    chosen = Column(Boolean, nullable=False)

    def __init__(self, name, family, login, chosen):
        self.name = name
        self.family = family
        self.login = login
        self.chosen = chosen

    def to_dict(self):
        dict = {}

        dict['name'] = self.name
        dict['family'] = self.family
        dict['login'] = self.login
        dict['chosen'] = self.chosen

        return dict
