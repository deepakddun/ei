from flask import Blueprint, request, render_template, url_for, redirect
from EIS.EISApp.child.forms import ChildRegistration, ChildAddress, FamilyInformation, DiagnosisInformation

child = Blueprint('child', __name__,url_prefix='/child',template_folder="../templates/child")


@child.route('/names', methods=['GET', 'POST'])
def child_basic():
    form = ChildRegistration()
    if form.validate_on_submit():
        return redirect(url_for('child.child_address'))
    return render_template('child_register.html', form=form, child_active='active')


@child.route('/address', methods=['GET', 'POST'])
def child_address():
    form = ChildAddress()
    if form.validate_on_submit():
        return redirect(url_for('child.child_family'))
    return render_template('child_address.html', form=form, address_active='active')


@child.route('/family', methods=['GET', 'POST'])
def child_family():
    form = FamilyInformation()
    if form.validate_on_submit():
        return redirect(url_for('child.child_diagnosis'))
    return render_template('child_family.html', form=form, family_active='active')


@child.route('/diag', methods=['GET', 'POST'])
def child_diagnosis():
    form = DiagnosisInformation()
    print('Testing')
    if form.validate_on_submit():
        return "<h1> Welcome back </h1>"
    return render_template('child_diagnosis.html', form=form, diagnosis_active='active')
