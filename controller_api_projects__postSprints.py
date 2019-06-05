from django.core import serializers
from models.fltrainb.sprint import sprint as Sprint
import json

class interna_postSprints():
    pass


# @class_declaration trainB_post #
class trainB_postSprints(interna_postSprints):

    @staticmethod
    def start(pk, data):
        if  'project' in data and  'improvement' in data and  'action' in data:
            try:
                if 'idsprint' in data:
                    Sprint().load({"idsprint":data['idsprint']}).update(data)
                else:
                    Sprint().create(data)
                result = {'result':'ok'}
            except Exception as e:
                result = {'result':'error', 'error': str(e)}
        else:
            result = {'result':'error', 'error': 'Datos insuficientes'}
        return result


# @class_declaration post #
class postSprints(trainB_postSprints):
    pass
