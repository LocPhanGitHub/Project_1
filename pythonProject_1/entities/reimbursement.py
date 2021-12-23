class Reimbursement:
    def __init__(self, request_id: int, user_id: int, expense_name: str, expense_amount: float, expense_detail: str,
                 status: str, user_comment: str):
        self.request_id = request_id
        self.user_id = user_id
        self.expense_name = expense_name
        self.expense_amount = expense_amount
        self.expense_detail = expense_detail
        self.status = status
        self.user_comment = user_comment

    def create_reimbursement_dictionary(self):
        return {
            "requestId": self.request_id,
            "userId": self.user_id,
            "expenseName": self.expense_name,
            "expenseAmount": self.expense_amount,
            "expenseDetail": self.expense_detail,
            "status": self.status,
            "userComment": self.user_comment,
        }

    def __str__(self):
        return "request ID: {}, user ID: {}, expense name: {}, expense amount: {}, expense detail: {}, status: {}, user comment: {}".format(
            self.request_id,
            self.user_id,
            self.expense_name,
            self.expense_amount,
            self.expense_detail,
            self.status,
            self.user_comment
        )
