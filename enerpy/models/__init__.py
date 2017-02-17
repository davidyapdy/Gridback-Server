"""
models
~~~~~~

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
import datetime

from sqlalchemy.dialects.mysql import INTEGER, DECIMAL, VARCHAR, MEDIUMTEXT, DATETIME

from enerpy import db


class Person(db.Model):
    id               = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    firstname        = db.Column(VARCHAR(40), nullable=False)
    lastname         = db.Column(VARCHAR(40), nullable=False)
    join_date        = db.Column(DATETIME, nullable=False, default=datetime.datetime.utcnow)
    email            = db.Column(VARCHAR(254), nullable=False)
    provider         = db.Column(INTEGER(unsigned=True), db.ForeignKey('Company.id'))


class Company(db.Model):
    id           = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    name         = db.Column(VARCHAR(512), nullable=False)
    phone_number = db.Column(VARCHAR(64))
    cycle        = db.Column(INTEGER())
    supply_rate  = db.Column()
    type         = db.Column()
    renewable    = db.Column()
    img          = db.Column()
    enrollment   = db.Column()
    cancellation = db.Column()
    customers    = db.relationship('Customers', backref="provider", cascade="all, delete-orphan", lazy='dynamic')
