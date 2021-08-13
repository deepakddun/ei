from flask import session
import datetime
import requests
import json
import random

form_data: dict = {}


def setValuesToRedis(form, form_type):
    details_dict: dict = {}

    key_value = session["key"]
    for key, value in form.data.items():
        if key not in ('csrf_token', 'submit'):
            print(key, value)
            print(type(value))
            if type(value) is datetime.date:
                value = str(value)
            if key == 'phone_number':
                print(value['country_code'])
                # session['country_code'] = value['country_code']
                # session['area_code'] = value['area_code']
                # session['number'] = value['number']
                details_dict['country_code'] = value['country_code']
                details_dict['area_code'] = value['area_code']
                details_dict['number'] = value['number']
            else:
                # session[key] = value
                details_dict[key] = value
    form_data[form_type] = details_dict
    key_value = {key_value: form_data}
    session.update(key_value)
    print(session.items())
    ##################################################################

    # url = "https://zn2kvypfi0.execute-api.us-east-2.amazonaws.com/Dev/add"
    #
    # data = requests.post(url, data = json.dumps(form_data))
    # print(json.dumps(form_data))
    # print(data.status_code)

    #################################################################
    # print(form_data)


def getValuesFromRedis(form, form_type=None):
    form_field: dict = {}
    key_value = session["key"]
    print(key_value)
    session_data = session.get(key_value, None)
    if session_data is not None:
        form_field = session_data.get(form_type, None)

    if form_field:
        for field in form:
            if field.name not in ('submit', 'csrf_token'):
                print(f"TESTINGGGG{field.name}")
                value = form_field.get(field.name, None)
                if field.name == 'child_dob' and value is not None:
                    field.data = datetime.datetime.strptime(value, '%Y-%m-%d')
                elif field.name == 'phone_number':
                    print("Inside phone number")
                    print(field.data)
                    field.country_code.data = form_field.get('country_code', None)
                    field.area_code.data = form_field.get('area_code', None)
                    field.number.data = form_field.get('number', None)
                else:
                    field.data = value
                print(field)
