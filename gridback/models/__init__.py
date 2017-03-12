"""
models/__init__.py
~~~~~~~~~~~~~~~~~~

Database model definition for a Person, a Provider (energy), and a Contract.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
from datetime import datetime

from sqlalchemy.dialects.mysql import (
    INTEGER, DECIMAL, VARCHAR, MEDIUMTEXT, DATETIME
)

from gridback import db
from gridback.models.http import BaseRequest, BaseResponse


class Person(db.Model):
    __tablename__ = 'person'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)
    joined        = db.Column(DATETIME, nullable=False, default=datetime.utcnow)
    email         = db.Column(VARCHAR(254), unique=True, nullable=False)
    state         = db.Column(VARCHAR(2), nullable=False)

    # one-one: person <--> contract
    contract      = db.relationship("Contract", uselist=False, back_populates="person")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def from_email(self, email):
        return Person.query.filter(Person.email == email).first()


class Provider(db.Model):
    __tablename__ = 'provider'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)
    name          = db.Column(VARCHAR(512))
    phone_number  = db.Column(VARCHAR(64))
    cycle         = db.Column(INTEGER())
    supply_rate   = db.Column(INTEGER(), nullable=False)
    pricing_model = db.Column(VARCHAR(32))
    renewable     = db.Column(INTEGER())
    img           = db.Column(VARCHAR(1024))
    enrollment    = db.Column(VARCHAR(256))
    cancellation  = db.Column(VARCHAR(256))

    contracts     = db.relationship('Contract', back_populates="provider")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Contract(db.Model):
    __tablename__ = 'contract'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)

    # one-one: person <--> contract
    person_id     = db.Column(INTEGER(unsigned=True), db.ForeignKey('person.id'))
    person        = db.relationship("Person", back_populates="contract")

    # one-many: contract <--> company
    provider_id   = db.Column(INTEGER(unsigned=True),
                              db.ForeignKey('provider.id'))
    provider      = db.relationship("Provider", back_populates="contracts")

    # current expiry/rate, does not match self.provider.expiry|rate
    expiry        = db.Column(DATETIME, nullable=False)
    rate          = db.Column(DECIMAL, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
