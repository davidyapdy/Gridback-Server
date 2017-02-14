from enerpy import db


class Person(db.Model):
    firstname = db.Column()
    lastname = db.Column()
    join_date = db.Column()
    email = db.Column()
    selected_company_id = db.Column()


class Company(db.Model):
    name = db.Column()
    phone_number = db.Column()
    cycle = db.Column()
    supply_rate = db.Column()
    type = db.Column()
    renewable = db.Column()
    img = db.Column()
    enrollment = db.Column()
    cancellation = db.Column()
