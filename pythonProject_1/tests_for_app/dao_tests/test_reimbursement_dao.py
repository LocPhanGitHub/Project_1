from datetime import datetime

from data_access_layer.implementation_classes.reimbursement_postgres_dao import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement

reimbursement_dao = ReimbursementPostgresDAO()

reimbursement: Reimbursement = Reimbursement(1, 1, "test", 100.00, "created for test", "pending", "no comment")

update_reimbursement = Reimbursement(1, 1, "test", 100.00, "created for update", "accepted", "updated successfully")

reimbursement_to_delete = Reimbursement(1, 1, "test", 100.00, "to be deleted", "accepted", "deleted")


def test_create_reimbursement_success():
    created_reimbursement = reimbursement_dao.create_reimbursement(reimbursement)
    assert created_reimbursement.request_id != 0


def test_get_reimbursement_by_request_id_success():
    get_reimbursement = reimbursement_dao.get_reimbursements_by_request_id(1)
    assert get_reimbursement.request_id == 1


def test_get_all_reimbursements_by_employee_id_success():
    get_reimbursement = reimbursement_dao.get_all_reimbursements_by_employee_id(1)
    assert len(get_reimbursement) >= 1


def test_get_all_reimbursements_success():
    reimbursements = reimbursement_dao.get_all_reimbursements()
    assert len(reimbursements) >= 2


def test_update_reimbursements_by_id_success():
    to_be_updated_reimbursement = reimbursement_dao.update_reimbursements_by_id(update_reimbursement)
    assert to_be_updated_reimbursement.status == update_reimbursement.status
    assert to_be_updated_reimbursement.user_comment == update_reimbursement.user_comment


def test_delete_reimbursement_success():
    reimbursement_to_be_deleted = reimbursement_dao.create_reimbursement(reimbursement_to_delete)
    result = reimbursement_dao.delete_reimbursement_by_request_id(reimbursement_to_be_deleted.request_id)
    assert result
