from sqlalchemy import Column, Integer, String, Boolean

from base import Base

class User(Base):
    """ User """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    family = Column(Boolean, nullable=False)
    login = Column(Boolean, nullable=False)
    chosen = Column(Boolean, nullable=False)
    gifting = Column(String(50), nullable=False)

    def __init__(self, name, family, login, chosen, gifting):
        self.name = name
        self.family = family
        self.login = login
        self.chosen = chosen
        self.gifting = gifting

    def to_dict(self):
        dict = {}

        dict['id'] = self.id
        dict['name'] = self.name
        dict['family'] = self.family
        dict['login'] = self.login
        dict['chosen'] = self.chosen
        dict['gifting'] = self.gifting

        return dict
