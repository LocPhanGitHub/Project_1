class NegativeValueReimbursementRequestException(Exception):
    def __init__(self, message):
        self.message = message


class NonNumericValueReimbursementRequestException(Exception):
    def __init__(self, message):
        self.message = message


class NonUpdatedStatusException(Exception):
    def __init__(self, message):
        self.message = message
