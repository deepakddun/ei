from botocore.exceptions import ClientError
from flask import session, flash
import datetime
import requests
import json
import random
from EIS.EISApp import db
from EIS.EISApp.model import Child, Address, FamilyInformationTB, Diagnosis, PhoneNumber
import traceback
import os
import boto3
from EIS.EISApp import logger

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


def save_to_db(session_data, key, child_basic, child_address, child_family, child_diagnosis):
    try:
        child_basic_details = session_data.get(child_basic)
        child_address_details = session_data.get(child_address)
        child_family_details = session_data.get(child_family)
        child_diagnosis_details = session_data.get(child_diagnosis)
        print(child_basic_details)
        print(child_address_details)
        print(child_family_details)
        print(child_diagnosis_details)

        child_model = Child(
            id=key,
            firstname=child_basic_details.get('child_firstname', None),
            middlename=child_basic_details.get('child_middlename', None),
            lastname=child_basic_details.get('child_lastname', None),
            child_dob=child_basic_details.get('child_dob', None),
            child_gender=child_basic_details.get('child_gender', None),
            status='Saved',

        )

        address_model = Address(
            address1=child_address_details.get('address1'),
            address2=child_address_details.get('address2'),
            county=child_address_details.get('county'),
            city=child_address_details.get('city'),
            state=child_address_details.get('state'),
            zip=child_address_details.get('zip'),
            child_address=child_model
        )
        family_model = FamilyInformationTB(
            mother_firstname=child_family_details.get('mother_firstname'),
            mother_last_name=child_family_details.get('mother_last_name'),
            father_first_name=child_family_details.get('father_first_name'),
            father_last_name=child_family_details.get('father_last_name'),
            email=child_family_details.get('email'),
            child_familyinfo=child_model
        )

        phonenumber_model = PhoneNumber(

            country_code=child_family_details.get('country_code'),
            area_code=child_family_details.get('area_code'),
            number=child_family_details.get('number'),
            child_phonenumber=child_model
        )

        child_diag_model = Diagnosis(
            details=child_diagnosis_details.get('details'),
            child_diagnosis=child_model
        )

        db.session.add(child_model)
        db.session.add(address_model)
        db.session.add(family_model)
        db.session.add(phonenumber_model)
        db.session.add(child_diag_model)
        db.session.commit()

        value = session.pop(key)
        print(f'Deleted value is {value}')
        flash(f"Application has been saved. {key} is the reference number","success")

    except Exception as e:
        db.session.rollback()
        flash("Error while saving data", "danger")
        traceback.print_exc()
        raise


def start_workflow(ref_number,first_name,middle_name,last_name):
    name = ""
    if middle_name:
        name = f"{first_name} {middle_name} {last_name}"
    else:
        name = f"{first_name} {last_name}"
    if os.environ.get('STEP_ARN'):
        start_stepfunction(os.environ.get('STEP_ARN'),
                           {"ref_number": ref_number, "child_name": name})
    pass


def start_stepfunction(step_function_arn, payload):
    try:
        step_function = boto3.client('stepfunctions')
        response = step_function.start_execution(stateMachineArn=step_function_arn,
                                                 input=json.dumps(payload)
                                                 )
        logger.info(f"Started step function {response['executionArn']}  at {response['startDate']}")
    except ClientError as e:
        logger.exception("Could created state machine")
        raise



