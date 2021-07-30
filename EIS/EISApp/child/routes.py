from flask import Blueprint, request, render_template, url_for, redirect
from EIS.EISApp.child.forms import ChildRegistration, ChildAddress, FamilyInformation, DiagnosisInformation
from EIS.EISApp.child.utils import setValuesToRedis , getValuesFromRedis
from EIS.EISApp import logger

child = Blueprint('child', __name__, url_prefix='/child', template_folder="../templates/child")


@child.route('/names', methods=['GET', 'POST'])
def child_basic():
    logger.info("Inside child registration")
    form = ChildRegistration()
    form_type = 'childregister'

    # for field in form:
    #     print(field.name)
    if form.validate_on_submit():
        setValuesToRedis(form,form_type)
        return redirect(url_for('child.child_address'))
    getValuesFromRedis(form, form_type)
    return render_template('child_register.html', form=form, child_active='active')


@child.route('/address', methods=['GET', 'POST'])
def child_address():
    logger.info("Inside child address")
    form = ChildAddress()
    print(request.method)
    if form.validate_on_submit():
        setValuesToRedis(form)
        return redirect(url_for('child.child_family'))
    getValuesFromRedis(form)
    return render_template('child_address.html', form=form, address_active='active')


@child.route('/family', methods=['GET', 'POST'])
def child_family():
    logger.info("Inside child family")
    form = FamilyInformation()
    if form.validate_on_submit():
        print('Testing')
        setValuesToRedis(form)
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
        setValuesToRedis(form)
        return "<h1> Welcome back </h1>"
    getValuesFromRedis(form)
    return render_template('child_diagnosis.html', form=form, diagnosis_active='active')




