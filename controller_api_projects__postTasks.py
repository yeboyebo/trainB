from django.core import serializers
from models.fltrainb.task import task as Task
import json

class interna_postTasks():
    pass


# @class_declaration trainB_post #
class trainB_postTasks(interna_postTasks):

    @staticmethod
    def start(pk, data):
        if  'sprint' in data:
            try:
                if 'idtask' in data:
                    Task().load({"idtask":data['idtask']}).update(data)
                else:
                    Task().create(data)
                result = {'result':'ok'}
            except Exception as e:
                result = {'result':'error', 'error': str(e)}
        else:
            result = {'result':'error', 'error': 'Datos insuficientes'}
        return result


# @class_declaration post #
class postTasks(trainB_postTasks):
    pass
