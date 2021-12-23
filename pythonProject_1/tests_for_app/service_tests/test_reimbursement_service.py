from custom_exceptions.reimbursement_exceptions import NegativeValueReimbursementRequestException, \
    NonNumericValueReimbursementRequestException, NonUpdatedStatusException
from data_access_layer.implementation_classes.reimbursement_postgres_dao import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.implementation_services.reimbursement_postgres_service import ReimbursementPostgresService

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement_service = ReimbursementPostgresService(reimbursement_dao)

reimbursement = Reimbursement(1, 1, "test", 100.00, "test service create", "pending", "")


def test_validate_negative_value_for_reimbursement_request():
    try:
        reimbursement_service.service_create_reimbursement(reimbursement)
    except NegativeValueReimbursementRequestException as e:
        assert str(e) == "You cannot make a request with negative value!"


def test_validate_non_numeric_value_for_reimbursement_request():
    try:
        reimbursement_service.service_create_reimbursement(reimbursement)
    except NonNumericValueReimbursementRequestException as e:
        assert str(e) == "You can only input numeric value into the reimbursement request!"


def test_validate_status_changed_by_manager():
    try:
        reimbursement_service.service_update_reimbursements_by_id(reimbursement)
    except NonUpdatedStatusException as e:
        assert str(e) == "You need to update the reimbursement status!"
