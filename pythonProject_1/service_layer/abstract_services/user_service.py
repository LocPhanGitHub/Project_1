from abc import ABC, abstractmethod

from entities.user import User


class UserService(ABC):
    @abstractmethod
    def service_login_into_account(self, user_name: str, user_password: str, user_role: str):
        pass

    @abstractmethod
    def service_create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def service_get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def service_get_all_user_by_id(self) -> list[User]:
        pass

    @abstractmethod
    def service_update_user_information(self, user: User) -> User:
        pass

    @abstractmethod
    def service_delete_user_by_id(self, user_id: int) -> bool:
        pass
