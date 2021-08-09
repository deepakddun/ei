from EIS.EISApp import db
from datetime import datetime


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    middlename = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    child_dob = db.Column(db.Date, nullable=False)
    child_gender = db.Column(db.String, nullable=False)
    lastwritten = db.Column(db.DateTime, default=datetime.utcnow)
    addresses = db.relationship('Address', backref='child', lazy=True)
    phonenumber = db.relationship('PhoneNumber', backref='child', lazy=True)
    familyInfo = db.relationship('FamilyInformation', backref='child', lazy=True)
    diagnosis = db.relationship('Diagnosis', backref='child', lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String, nullable=False)
    address2 = db.Column(db.String, nullable=True)
    county = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.Integer, nullable=True)
    area_code = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)


class FamilyInformation(db.Model):
    mother_firstname = db.Column(db.String, nullable=False)
    mother_last_name = db.Column(db.String, nullable=False)
    father_first_name = db.Column(db.String, nullable=False)
    father_last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    person_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)


class Diagnosis(db.Model):
    details = db.Column(db.Text, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
