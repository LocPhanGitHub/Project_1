from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDAO
from entities.user import User

user_dao = UserPostgresDAO()

new_user = User("new", "user", "manager", 1, "new_username", "new_password")

update_user = User("update", "user", "manager", 1, "new_update_username", "new_update_password")

delete_user = User("deleted", "customer", "employee", 2, "deleted_username", "deleted_password")


def test_validate_login():
    validated = user_dao.login_into_account(new_user.user_name, new_user.user_password, new_user.user_role)
    assert validated[0] == 6


def test_not_valid_login():
    validated = user_dao.login_into_account("bad username", "bad password", "not employee")
    assert validated is None


def test_create_user_success():
    user_result = user_dao.create_user(new_user)
    assert user_result.user_id != 0


def test_get_user_by_id_success():
    initial_user = user_dao.get_user_by_id(1)
    assert initial_user.user_id == 1


def test_get_all_user_by_id_success():
    users = user_dao.get_all_user_by_id()
    assert len(users) >= 1


def test_update_user_by_id_success():
    to_be_updated_user = user_dao.update_user_by_id(update_user)
    assert to_be_updated_user.user_name == update_user.user_name
    assert to_be_updated_user.user_password == update_user.user_password


def test_delete_user_by_id_success():
    to_be_deleted = user_dao.create_user(delete_user)
    result = user_dao.delete_user_by_id(to_be_deleted.user_id)
    assert result
