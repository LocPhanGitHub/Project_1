from data_access_layer.abstract_classes.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class ReimbursementPostgresDAO(ReimbursementDAO):

    def create_reimbursement(self, reimbursement: Reimbursement):
        sql = "insert into reimbursement values(default, %s, %s, %s, %s, %s, %s) returning request_id"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.user_id, reimbursement.expense_name, reimbursement.expense_amount,
                             reimbursement.expense_detail, reimbursement.status,
                             reimbursement.user_comment))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        reimbursement.request_id = generated_id
        return reimbursement

    def get_reimbursements_by_request_id(self, request_id: int):
        sql = "select * from reimbursement where request_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])
        reimbursement_record = cursor.fetchone()
        reimbursement = Reimbursement(*reimbursement_record)
        return reimbursement

    def get_all_reimbursements_by_employee_id(self, user_id: int):
        sql = "select * from reimbursement where user_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def get_all_reimbursements(self):
        sql = "select * from reimbursement"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def update_reimbursements_by_id(self, reimbursement: Reimbursement):
        sql = "update reimbursement set status = %s, user_comment = %s where request_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.status, reimbursement.user_comment, reimbursement.request_id))
        connection.commit()
        return reimbursement

    def delete_reimbursement_by_request_id(self, request_id: int) -> bool:
        sql = "delete from reimbursement where request_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])
        connection.commit()
        return True
