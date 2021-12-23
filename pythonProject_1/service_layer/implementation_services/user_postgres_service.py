from custom_exceptions.user_exceptions import DuplicateCreateUserNameException, DuplicateUpdateUserNameException
from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDAO
from entities.user import User
from service_layer.abstract_services.user_service import UserService


class UserPostgresService(UserService):
    def __init__(self, user_dao: UserPostgresDAO):
        self.user_dao = user_dao

    def service_login_into_account(self, user_name: str, user_password: str, user_role: str):
        validation = self.user_dao.login_into_account(user_name, user_password, user_role)
        if type(validation) == tuple:
            return True
        else:
            return False

    def service_create_user(self, user: User) -> User:
        users = self.user_dao.get_all_user_by_id()
        for existing_user in users:
            if existing_user.user_id != user.user_id:
                if existing_user.user_name == user.user_name:
                    raise DuplicateCreateUserNameException(
                        "You cannot use that user name: It has already been created!")
        created_user = self.user_dao.create_user(user)
        return created_user

    def service_get_user_by_id(self, user_id: int) -> User:
        return self.user_dao.get_user_by_id(user_id)

    def service_get_all_user_by_id(self) -> list[User]:
        return self.user_dao.get_all_user_by_id()

    def service_update_user_information(self, user: User) -> User:
        users = self.user_dao.get_all_user_by_id()
        for current_user in users:
            if current_user.user_id == user.user_id:
                if current_user.user_name == user.user_name:
                    raise DuplicateUpdateUserNameException("You cannot use that username: It is already taken!")
        updated_user = self.user_dao.update_user_by_id(user)
        return updated_user

    def service_delete_user_by_id(self, user_id: int) -> bool:
        return self.user_dao.delete_user_by_id(user_id)
