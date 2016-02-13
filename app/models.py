from datetime import datetime

from sqlalchemy import Column

from app import db


class Person(db.Model):
    """
    Representing a Person detail.
    1) name    4) City
    2) email   5) Company
    3) Contact
    """

    __tablename__ = 'Person'

    id = Column(db.Integer, primary_key=True)
    added = Column(db.DateTime, default=datetime.now)

    name = Column(db.String(40))
    email = Column(db.String(40))
    contact = Column(db.String(20))
    city = Column(db.String(20))
    company = Column(db.String(40))

    def __init__(self , name  , email , contact, city, company):
        self.name = name
        self.email = email
        self.contact = contact
        self.city = city
        self.company = company

    def __repr__(self):
        """
        String representation of Person Object
         <Vishnu A Venu: Jlabs>
        """
        return (u'<{self.name} : {self.company}>')
