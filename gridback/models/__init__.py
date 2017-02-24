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


class Person(db.Model):
    __tablename__ = 'person'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)
    joined        = db.Column(DATETIME, nullable=False,
                              default=datetime.datetime.utcnow)
    email         = db.Column(VARCHAR(254), nullable=False)
    provider      = db.Column(INTEGER(unsigned=True),
                              db.ForeignKey('Company.id'))
    contract_id   = db.Column(INTEGER(unsigned=True), )
    contract      = db.Column()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Contract(db.Model):
    __tablename__ = 'contract'
    id            = db.Column(INTEGER(unsigned=True), primary_key=True)
    person_id     = db.Column()
    person        = db.Column()
    expiry        = db.Column()
    rate          = db.Column()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Company(db.Model):
    __tablename__ = 'company'
    id           = db.Column(INTEGER(unsigned=True), primary_key=True)
    name         = db.Column(VARCHAR(512), nullable=False)
    phone_number = db.Column(VARCHAR(64))
    cycle        = db.Column(INTEGER(), nullable=False)
    supply_rate  = db.Column(INTEGER(), nullable=False)
    type         = db.Column(VARCHAR(32), nullable=False)
    renewable    = db.Column(INTEGER(), nullable=False)
    img          = db.Column(VARCHAR(1024))
    enrollment   = db.Column(VARCHAR(256))
    cancellation = db.Column(VARCHAR(256))
    customers    = db.relationship('Customers', backref="provider",
                                   cascade="all, delete-orphan", lazy='dynamic')

    def as_dict(self):
        return {c.name:getattr(self, c.name) for c in self.__table__.columns}


db.create_all()
