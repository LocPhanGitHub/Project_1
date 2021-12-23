from abc import ABC, abstractmethod

from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):
    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def get_reimbursements_by_request_id(self, request_id: int):
        pass

    @abstractmethod
    def get_all_reimbursements_by_employee_id(self, user_id: int):
        pass

    @abstractmethod
    def get_all_reimbursements(self):
        pass

    @abstractmethod
    def update_reimbursements_by_id(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def delete_reimbursement_by_request_id(self, request_id: int) -> bool:
        pass
