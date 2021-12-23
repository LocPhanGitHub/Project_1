class DuplicateCreateUserNameException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicateUpdateUserNameException(Exception):
    def __init__(self, message: str):
        self.message = message
