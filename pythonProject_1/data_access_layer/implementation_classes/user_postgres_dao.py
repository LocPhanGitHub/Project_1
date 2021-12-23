from data_access_layer.abstract_classes.user_dao import UserDAO
from entities.user import User
from util.database_connection import connection


class UserPostgresDAO(UserDAO):
    def login_into_account(self, user_name: str, user_password: str, user_role: str):
        sql = "select user_id from user_information where user_name = %s and user_password = %s and user_role = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (user_name, user_password, user_role))
        validated = cursor.fetchone()
        return validated

    def create_user(self, user: User) -> User:
        sql = "insert into user_information values(%s, %s, %s, default, %s, %s) returning user_id"
        cursor = connection.cursor()
        cursor.execute(sql, (user.first_name, user.last_name, user.user_role, user.user_name, user.user_password))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        user.user_id = generated_id
        return user

    def get_user_by_id(self, user_id: int) -> User:
        sql = "select * from user_information where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        user_record = cursor.fetchone()
        user = User(*user_record)
        return user

    def get_all_user_by_id(self) -> list[User]:
        sql = "select * from user_information"
        cursor = connection.cursor()
        cursor.execute(sql)
        user_records = cursor.fetchall()
        users = []
        for user in user_records:
            users.append(User(*user))
        return users

    def update_user_by_id(self, user: User) -> User:
        sql = "update user_information set user_name = %s, user_password = %s where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (user.user_name, user.user_password, user.user_id))
        connection.commit()
        return user

    def delete_user_by_id(self, user_id: int) -> bool:
        sql = "delete from user_information where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        return True
