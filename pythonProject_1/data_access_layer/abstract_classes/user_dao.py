from abc import ABC, abstractmethod

from entities.user import User


class UserDAO(ABC):

    @abstractmethod
    def login_into_account(self, user_name: str, user_password: str, user_role: str):
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all_user_by_id(self) -> list[User]:
        pass

    @abstractmethod
    def update_user_by_id(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user_by_id(self, user_id: int) -> bool:
        pass
