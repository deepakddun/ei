from flask import Blueprint, request, render_template, url_for, redirect, session
from EIS.EISApp.child.forms import ChildRegistration, ChildAddress, FamilyInformation, DiagnosisInformation
from EIS.EISApp.child.utils import setValuesToRedis, getValuesFromRedis, save_to_db
from EIS.EISApp import logger
from EIS.EISApp import key
from EIS.EISApp import db
from EIS.EISApp.model import Child
import random

child = Blueprint('child', __name__, url_prefix='/child', template_folder="../templates/child")


# @child.route('/names')
# def return_key():
#     logger.info("IN RETURN KEY FUNCTION")
#     form = ChildRegistration()
#     value = session.get("key",None)
#     if value is None:
#         session["key"] = random.randint(12457, 999998)
#     print(session["key"])
#     print(session.keys())
#     return render_template('child_register.html', form=form, child_active='active')


def setSessionKey():
    logger.info("setsessionkey")
    value = session.get("key", None)
    if value is None:
        session["key"] = random.randint(12457, 999998)


@child.route('/names', methods=['GET', 'POST'])
def child_basic():
    setSessionKey()
    logger.info(f"Inside child registration {key}")

    form = ChildRegistration()

    # for field in form:
    #     print(field.name)
    if form.validate_on_submit():
        setValuesToRedis(form, child_basic.__name__)
        return redirect(url_for('child.child_address'))
    getValuesFromRedis(form, child_basic.__name__)
    return render_template('child_register.html', form=form, child_active='active')


@child.route('/address', methods=['GET', 'POST'])
def child_address():
    logger.info("Inside child address")
    form = ChildAddress()
    print(request.method)
    if form.validate_on_submit():
        setValuesToRedis(form, child_address.__name__)

        return redirect(url_for('child.child_family'))
    getValuesFromRedis(form, child_address.__name__)
    return render_template('child_address.html', form=form, address_active='active')


@child.route('/family', methods=['GET', 'POST'])
def child_family():
    logger.info("Inside child family")
    form = FamilyInformation()
    if form.validate_on_submit():
        print('Testing')
        setValuesToRedis(form, child_family.__name__)
        return redirect(url_for('child.child_diagnosis'))
    print('pinting 2')
    getValuesFromRedis(form, child_family.__name__)
    return render_template('child_family.html', form=form, family_active='active')


@child.route('/diagnosis', methods=['GET', 'POST'])
def child_diagnosis():
    logger.info("Inside child diagnosis")
    form = DiagnosisInformation()
    session_key = session.get("key", None)
    print('Testing')
    if form.validate_on_submit():
        setValuesToRedis(form, child_diagnosis.__name__)
        return render_template('submit_form.html', form=form, key=session_key)
    getValuesFromRedis(form, child_diagnosis.__name__)
    return render_template('child_diagnosis.html', form=form, diagnosis_active='active')


@child.route('/save_data/<int:key>', methods=['POST'])
def save_data(key):
    session_data = session.get(key, None)
    if session_data:
        save_to_db(session_data, key, child_basic.__name__, child_address.__name__, child_family.__name__,
                   child_diagnosis.__name__)

    return "<h1> DATA SAVED </h1>"


@child.route('/child/list', methods=['GET'])
def list_saved_children():
    page = request.args.get('page', 1, type=int)
    print(page)
    children = Child.query.order_by(Child.lastwritten.desc()).paginate(page=page, per_page=4)
    print(children.total)
    return render_template('child_list.html', children=children)


@child.route('/child/get/<int:key>', methods=['GET'])
def get_child(key):
    child_details = Child.query.get(key)
    print(child_details.addresses.address1)
    return "Happy"
