from sqlalchemy import event

from EIS.EISApp.model import Child
import pytest
from datetime import date
from flask import url_for


def test_new_user():
    """
        GIVEN  a Child Model
        WHEN a new child record is created
        THEN check the first and last name
    """
    child = Child(id=1,
                  firstname='Test',
                  middlename='Test',
                  lastname='Test',
                  child_dob=date.today(),
                  child_gender='M',
                  status='Saved')

    assert child.id == 1 and child.firstname == 'Test'


def test_ping(app):
    """
    GIVEN : a application client
    WHEN : the home page is accessed
    THEN : a proper response is received
    """
    assert app.test_client().get(url_for('main.home')).status_code == 200
    assert "Welcome to the project" in app.test_client().get(url_for('main.home')).get_data(as_text=True)


def test_child_data(app):
    response = app.test_client().post(url_for('child.child_basic'), data={
        "child_firstname": "Test",
        "child_middlename": "Test",
        "child_lastname": "Test",
        "child_dob": date.today(),
        "child_gender": "M"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert "Address Line 2" in response.get_data(as_text=True)


def test_a_transaction(db_session):
    row = db_session.query(Child).get(71488)
    assert row.firstname == 'Alpha'


def test_child_transaction(db_session):
    child = Child(id=1,
                  firstname='Tumbin',
                  middlename='Test',
                  lastname='Test',
                  child_dob=date.today(),
                  child_gender='M',
                  status='Saved')
    db_session.add(child)
    db_session.commit()
    row = db_session.query(Child).get(1)
    print(row.firstname)
    assert True