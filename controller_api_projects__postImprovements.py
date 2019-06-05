from django.core import serializers
from models.fltrainb.improvement import improvement as Improvement
from django.db import transaction


class interna_postImprovements():
    pass


# @class_declaration trainB_post #
class trainB_postImprovements(interna_postImprovements):

    @staticmethod
    def start(pk, data):
        if  'project' in data:
            sid = transaction.savepoint()
            try:
                transaction.savepoint_rollback(sid)
                if "idimprovement" in data:
                    Improvement().load({"idimprovement": data["idimprovement"]}).update(data)
                else:
                    Improvement().create(data)
                result = {'result':'ok'}
                transaction.savepoint_commit(sid)
            except Exception as e:
                transaction.savepoint_rollback(sid)
                result = {'result':'error', 'error': str(e)}
        else:
            result = {'result':'error', 'error': 'Datos insuficientes'}
        return result


# @class_declaration post #
class postImprovements(trainB_postImprovements):
    pass
