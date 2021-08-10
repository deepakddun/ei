from flask import Blueprint, request, render_template, url_for, redirect, session
from EIS.EISApp.child.forms import ChildRegistration, ChildAddress, FamilyInformation, DiagnosisInformation
from EIS.EISApp.child.utils import setValuesToRedis, getValuesFromRedis
from EIS.EISApp import logger
from EIS.EISApp import key
import random
from EIS.EISApp.model import Child , Address ,FamilyInformationTB , Diagnosis , PhoneNumber

child = Blueprint('child', __name__, url_prefix='/child', template_folder="../templates/child")


@child.route('/names')
def return_key():
    logger.info("IN RETURN KEY FUNCTION")
    form = ChildRegistration()
    value = session.get("key",None)
    if value is None:
        session["key"] = random.randint(12457, 999998)
    print(session["key"])
    print(session.keys())
    return render_template('child_register.html', form=form, child_active='active')


@child.route('/names', methods=['GET', 'POST'])
def child_basic():
    logger.info(f"Inside child registration {key}")

    form = ChildRegistration()
    form_type = 'childregister'

    # for field in form:
    #     print(field.name)
    if form.validate_on_submit():
        setValuesToRedis(form, child_basic.__name__)
        return redirect(url_for('child.child_address'))
    getValuesFromRedis(form, form_type)
    return render_template('child_register.html', form=form, child_active='active')


@child.route('/address', methods=['GET', 'POST'])
def child_address():
    logger.info("Inside child address")
    form = ChildAddress()
    print(request.method)
    if form.validate_on_submit():
        setValuesToRedis(form, child_address.__name__)

        return redirect(url_for('child.child_family'))
    getValuesFromRedis(form)
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
    getValuesFromRedis(form)
    return render_template('child_family.html', form=form, family_active='active')


@child.route('/diagnosis', methods=['GET', 'POST'])
def child_diagnosis():
    logger.info("Inside child diagnosis")
    form = DiagnosisInformation()
    print('Testing')
    if form.validate_on_submit():
        setValuesToRedis(form, child_diagnosis.__name__)
        return "<h1> Welcome back </h1>"
    getValuesFromRedis(form)
    return render_template('child_diagnosis.html', form=form, diagnosis_active='active')
