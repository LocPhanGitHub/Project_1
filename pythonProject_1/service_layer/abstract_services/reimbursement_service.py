from abc import ABC, abstractmethod

from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):
    @abstractmethod
    def service_create_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_get_reimbursements_by_request_id(self, request_id: int):
        pass

    @abstractmethod
    def service_get_all_reimbursements_by_employee_id(self, user_id: int):
        pass

    @abstractmethod
    def service_get_all_reimbursements(self):
        pass

    @abstractmethod
    def service_update_reimbursements_by_id(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_delete_reimbursement_by_request_id(self, request_id: int) -> bool:
        pass
