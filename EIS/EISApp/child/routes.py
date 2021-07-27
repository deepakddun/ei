from flask import Blueprint, request, render_template, url_for
from EIS.EISApp.child.forms import ChildRegistration

child = Blueprint('child', __name__)


@child.route('/register', methods=['GET', 'POST'])
def register_child():
    form = ChildRegistration()
    return render_template('child_register.html', form=form)
