from flask import session
import datetime
import requests
import json

form_data:dict={}


def setValuesToRedis(form, form_type):
    details_dict={}
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
                details_dict['country_code'] = value['country_code']
                details_dict['area_code'] = value['area_code']
                details_dict['number'] = value['number']
            else:
                session[key] = value
                details_dict[key] = value
    form_data[form_type]= details_dict
    ##################################################################

    # url = "https://zn2kvypfi0.execute-api.us-east-2.amazonaws.com/Dev/add"
    #
    # data = requests.post(url, data = json.dumps(form_data))
    # print(json.dumps(form_data))
    # print(data.status_code)

    #################################################################
    print(form_data)



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


