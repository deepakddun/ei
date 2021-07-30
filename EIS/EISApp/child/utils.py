from flask import session
import datetime


def setValuesToRedis(form, form_type=None):
    for key, value in form.data.items():
        if key not in ('csrf_token', 'submit'):
            print(key, value)
            print(type(value))
            if type(value) is datetime.date:
                value = str(value)
            if key == 'phone_number':
                print(value['country_code'])
                session['country_code'] = value['country_code']
                session['area_code'] = value['area_code']
                session['number'] = value['number']
            else:
                session[key] = value


def getValuesFromRedis(form, form_type=None):
    for field in form:
        if field.name not in ('submit','csrf_token'):

            value = session.get(field.name,None)
            print(field.name,value)
            if value is not None:
                if field.name == 'child_dob' and value is not None:
                    field.data = datetime.datetime.strptime(value,'%Y-%m-%d')
                elif field.name == 'phone_number':
                    field.country_code.data = session.get('country_code', None)
                    field.area_code.data = session.get('area_code', None)
                    field.number.data = session.get('number', None)
                else:
                    field.data = value


