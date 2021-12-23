from custom_exceptions.user_exceptions import DuplicateCreateUserNameException, DuplicateUpdateUserNameException
from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDAO
from entities.user import User
from service_layer.implementation_services.user_postgres_service import UserPostgresService

user_dao = UserPostgresDAO()
user_service = UserPostgresService(user_dao)

bad_user = User("bad", "customer", "employee", 2, "bad_name", "bad_password")
bad_update_user = User("bad", "update customer", "employee", 2, "bad_update_name", "bad_update_password")

user_name = "new_username"
user_password = "new_password"
user_role = "manager"


def test_catch_creating_user_with_duplicate_username():
    try:
        user_service.service_create_user(bad_user)
    except DuplicateCreateUserNameException as e:
        assert str(e) == "You cannot use that user name: It has already been created!"


def test_catch_updating_user_with_duplicate_username():
    try:
        user_service.service_update_user_information(bad_update_user)
    except DuplicateUpdateUserNameException as e:
        assert str(e) == "You cannot use that username: It is already taken!"


def test_validate_correct_credentials():
    validation = user_service.service_login_into_account(user_name, user_password, user_role)
    assert validation


def test_catch_bad_username():
    validation = user_service.service_login_into_account('bad username', user_password, user_role)
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_password():
    validation = user_service.service_login_into_account(user_name, 'bad password', user_role)
    if validation:
        assert False
    else:
        assert True


def test_catch_not_employee():
    validation = user_service.service_login_into_account(user_name, user_password, 'not employee')
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_username_and_password():
    validation = user_service.service_login_into_account('bad username', 'bad password', 'not employee')
    if validation:
        assert False
    else:
        assert True
