"""
models
~~~~~~

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
import datetime

from sqlalchemy.dialects.mysql import (
    INTEGER, DECIMAL, VARCHAR, MEDIUMTEXT, DATETIME
)

from gridback import db


db.drop_all()


class Model(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Person(Model):
    __tablename__ = 'person'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)
    joined        = db.Column(DATETIME, nullable=False,
                              default=datetime.datetime.utcnow)
    email         = db.Column(VARCHAR(254), nullable=False)
    # one-one: person <--> contract
    contract      = db.relationship("Contract", uselist=False, back_populates="person")


class Contract(Model):
    __tablename__ = 'contract'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)

    # one-one: contract <--> company
    person_id     = db.Column(INTEGER(unsigned=True), db.ForeignKey('person.id'))
    person        = db.relationship("Person", back_populates="contract")

    provider_id   = db.Column(INTEGER(unsigned=True),
                              db.ForeignKey('provider.id'))
    expiry        = db.Column(DATETIME, nullable=False)
    rate          = db.Column(DECIMAL, nullable=False)


class Provider(Model):
    __tablename__ = 'provider'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)
    name          = db.Column(VARCHAR(512), nullable=False)
    phone_number  = db.Column(VARCHAR(64))
    cycle         = db.Column(INTEGER(), nullable=False)
    supply_rate   = db.Column(INTEGER(), nullable=False)
    type          = db.Column(VARCHAR(32), nullable=False)
    renewable     = db.Column(INTEGER(), nullable=False)
    img           = db.Column(VARCHAR(1024))
    enrollment    = db.Column(VARCHAR(256))
    cancellation  = db.Column(VARCHAR(256))
    customers     = db.relationship('Customers', backref="provider",
                                   cascade="all, delete-orphan", lazy='dynamic')


db.create_all()
