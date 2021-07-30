from flask import Blueprint, request, render_template, url_for, redirect
from EIS.EISApp.child.forms import ChildRegistration, ChildAddress, FamilyInformation, DiagnosisInformation
from EIS.EISApp import redis_client

child = Blueprint('child', __name__,url_prefix='/child',template_folder="../templates/child")


@child.route('/names', methods=['GET', 'POST'])
def child_basic():
    form = ChildRegistration()

    print(redis_client.get('Shree'))
    if form.validate_on_submit():
        for i in form.data.items():
            print(i)
        return redirect(url_for('child.child_address'))

    return render_template('child_register.html', form=form, child_active='active')


@child.route('/address', methods=['GET', 'POST'])
def child_address():
    form = ChildAddress()
    print(request.method)
    if form.validate_on_submit():
        return redirect(url_for('child.child_family'))
    return render_template('child_address.html', form=form, address_active='active')


@child.route('/family', methods=['GET', 'POST'])
def child_family():
    form = FamilyInformation()
    if form.validate_on_submit():
        print('Testing')
        return redirect(url_for('child.child_diagnosis'))
    print('pinting 2')
    return render_template('child_family.html', form=form, family_active='active')


@child.route('/diagnosis', methods=['GET', 'POST'])
def child_diagnosis():
    form = DiagnosisInformation()
    print('Testing')
    if form.validate_on_submit():
        return "<h1> Welcome back </h1>"
    return render_template('child_diagnosis.html', form=form, diagnosis_active='active')

def setValuesToRedis(form):
   
