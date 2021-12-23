class User:
    def __init__(self, first_name: str, last_name: str, user_role: str, user_id: int, user_name: str, user_password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.user_role = user_role
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password

    def __str__(self):
        return "first name: {}, last name: {}, user role: {}, user ID: {}, user name: {}, user password: {}".format(
            self.first_name, self.last_name, self.user_role, self.user_id, self.user_name, self.user_password
        )

    def create_user_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "userRole": self.user_role,
            "userId": self.user_id,
            "userName": self.user_name,
            "userPassword": self.user_password
        }
