from custom_exceptions.reimbursement_exceptions import NegativeValueReimbursementRequestException, \
    NonNumericValueReimbursementRequestException, NonUpdatedStatusException
from data_access_layer.implementation_classes.reimbursement_postgres_dao import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.abstract_services.reimbursement_service import ReimbursementService


class ReimbursementPostgresService(ReimbursementService):
    def __init__(self, reimbursement_dao: ReimbursementPostgresDAO):
        self.reimbursement_dao = reimbursement_dao

    def service_create_reimbursement(self, reimbursement: Reimbursement):
        reimbursements = self.reimbursement_dao.get_all_reimbursements()
        for existing_reimbursement in reimbursements:
            if existing_reimbursement.expense_amount <= 0:
                raise NegativeValueReimbursementRequestException("You cannot make a request with negative value!")
            if type(reimbursement.expense_amount) != float:
                raise NonNumericValueReimbursementRequestException("You can only input numeric value into the reimbursement request!")
        created_reimbursement = self.reimbursement_dao.create_reimbursement(reimbursement)
        return created_reimbursement

    def service_get_reimbursements_by_request_id(self, request_id: int):
        return self.reimbursement_dao.get_reimbursements_by_request_id(request_id)

    def service_get_all_reimbursements_by_employee_id(self, user_id: int):
        return self.reimbursement_dao.get_all_reimbursements_by_employee_id(user_id)

    def service_get_all_reimbursements(self):
        return self.reimbursement_dao.get_all_reimbursements()

    def service_update_reimbursements_by_id(self, reimbursement: Reimbursement):
        reimbursements = self.reimbursement_dao.get_all_reimbursements()
        for current_reimbursement in reimbursements:
            if current_reimbursement.request_id == reimbursement.request_id:
                if current_reimbursement.status == reimbursement.status:
                    raise NonUpdatedStatusException("You need to update the reimbursement status!")
        updated_reimbursement = self.reimbursement_dao.update_reimbursements_by_id(reimbursement)
        return updated_reimbursement

    def service_delete_reimbursement_by_request_id(self, request_id: int) -> bool:
        return self.reimbursement_dao.delete_reimbursement_by_request_id(request_id)
