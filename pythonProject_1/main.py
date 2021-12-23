from flask import Flask, request, jsonify
from flask_cors import CORS

import logging

from custom_exceptions.reimbursement_exceptions import NegativeValueReimbursementRequestException, \
    NonNumericValueReimbursementRequestException, NonUpdatedStatusException
from custom_exceptions.user_exceptions import DuplicateCreateUserNameException, DuplicateUpdateUserNameException
from data_access_layer.implementation_classes.reimbursement_postgres_dao import ReimbursementPostgresDAO
from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDAO
from entities.reimbursement import Reimbursement
from entities.user import User
from service_layer.implementation_services.reimbursement_postgres_service import ReimbursementPostgresService
from service_layer.implementation_services.user_postgres_service import UserPostgresService

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")
app: Flask = Flask(__name__)
CORS(app)

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement_service = ReimbursementPostgresService(reimbursement_dao)
user_dao = UserPostgresDAO()
user_service = UserPostgresService(user_dao)


@app.get("/")
def landing_page():
    return "This is the landing page"


# Reimbursement
@app.post("/reimbursement")
def create_reimbursement():
    try:
        reimbursement_data = request.get_json()
        new_reimbursement = Reimbursement(
            0,
            int(reimbursement_data["userId"]),
            reimbursement_data["expenseName"],
            float(reimbursement_data["expenseAmount"]),
            reimbursement_data["expenseDetail"],
            reimbursement_data["status"],
            reimbursement_data["userComment"]
        )
        reimbursement_to_return = reimbursement_service.service_create_reimbursement(new_reimbursement)
        reimbursement_as_dictionary = reimbursement_to_return.create_reimbursement_dictionary()
        account_as_json = jsonify(reimbursement_as_dictionary)
        return account_as_json, 200
    except NegativeValueReimbursementRequestException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400
    except NonNumericValueReimbursementRequestException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


@app.get("/reimbursement/<request_id>")
def get_reimbursements_by_request_id(request_id: str):
    result = reimbursement_service.service_get_reimbursements_by_request_id(int(request_id))
    result_as_dictionary = result.create_reimbursement_dictionary()
    account_as_json = jsonify(result_as_dictionary)
    return account_as_json


@app.get("/reimbursement/user/<user_id>")
def get_all_reimbursements_by_employee_id(user_id: str):
    reimbursements_as_reimbursements = reimbursement_service.service_get_all_reimbursements_by_employee_id(int(user_id))
    reimbursements_as_dictionary = []
    for reimbursements in reimbursements_as_reimbursements:
        dictionary_reimbursement = reimbursements.create_reimbursement_dictionary()
        reimbursements_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursements_as_dictionary)


@app.get("/reimbursement")
def get_all_reimbursements():
    reimbursements_as_reimbursements = reimbursement_service.service_get_all_reimbursements()
    reimbursements_as_dictionary = []
    for reimbursements in reimbursements_as_reimbursements:
        dictionary_reimbursement = reimbursements.create_reimbursement_dictionary()
        reimbursements_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursements_as_dictionary)


@app.patch("/reimbursement/<request_id>")
def update_reimbursement(request_id: str):
    try:
        body = request.get_json()
        update_info = Reimbursement(
            int(request_id),
            int(body["userId"]),
            body["expenseName"],
            float(body["expenseAmount"]),
            body["expenseDetail"],
            body["status"],
            body["userComment"]
        )
        updated_reimbursement = reimbursement_service.service_update_reimbursements_by_id(update_info)
        updated_reimbursement_as_dictionary = updated_reimbursement.create_reimbursement_dictionary()
        return jsonify(updated_reimbursement_as_dictionary), 200
    except NonUpdatedStatusException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.delete("/reimbursement/<request_id>")
def delete_reimbursement_by_request_id(request_id: str):
    result = reimbursement_service.service_delete_reimbursement_by_request_id(int(request_id))
    if result:
        return "Reimbursement with ID {} was deleted successfully".format(request_id)
    else:
        return "Something went wrong: Reimbursement with ID {} was not deleted".format(request_id)


# User
# LOGGING IN
@app.post("/login")
def login():
    body = request.get_json()
    login_credentials = (body["userName"], body["userPassword"], body["userRole"])
    validated = user_service.service_login_into_account(login_credentials[0], login_credentials[1], login_credentials[2])
    if validated:
        message = {"validated": True}
        return jsonify(message), 200
    else:
        message = {"validated": False}
        return jsonify(message), 400


@app.post("/user")
def create_user():
    try:
        body = request.get_json()
        new_user = User(
            body["firstName"],
            body["lastName"],
            body["userRole"],
            0,
            body["userName"],
            body["userPassword"]
        )
        created_user = user_service.service_create_user(new_user)
        created_user_as_dictionary = created_user.create_user_dictionary()
        return jsonify(created_user_as_dictionary), 200
    except DuplicateCreateUserNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/user/<user_id>")
def get_user_by_id(user_id: str):
    user = user_service.service_get_user_by_id(int(user_id))
    user_as_dictionary = user.create_user_dictionary()
    return jsonify(user_as_dictionary), 200


@app.get("/user")
def get_all_user_by_id():
    users = user_service.service_get_all_user_by_id()
    users_as_dictionaries = []
    for user in users:
        dictionary_user = user.create_user_dictionary()
        users_as_dictionaries.append(dictionary_user)
    return jsonify(users_as_dictionaries), 200


@app.patch("/user/<user_id>")
def update_user(user_id: str):
    try:
        body = request.get_json()
        update_info = User(
            body["firstName"],
            body["lastName"],
            body["userRole"],
            int(user_id),
            body["userName"],
            body["userPassword"]
        )
        updated_user = user_service.service_update_user_information(update_info)
        updated_user_as_dictionary = updated_user.create_user_dictionary()
        return jsonify(updated_user_as_dictionary), 200
    except DuplicateUpdateUserNameException as e:
        return str(e), 400


@app.delete("/user/<user_id>")
def delete_user(user_id: str):
    result = user_service.service_delete_user_by_id(int(user_id))
    if result:
        return f"User with ID {user_id} was deleted successfully"
    else:
        return f"Something went wrong. User with ID {user_id} was not deleted"


app.run()
