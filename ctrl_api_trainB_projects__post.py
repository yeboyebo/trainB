from django.core import serializers
from models.fltrainb.project import project as Project
import json

class interna_post():
    pass


# @class_declaration trainB_post #
class trainB_post(interna_post):

    @staticmethod
    def start(pk, data):
        if  'consultant' in data:
            try:
                if "idproject" in data:
                    Project().load({"idproject":data["idproject"]}).update(data)
                else:
                    Project().create(data)
                result = {'result':'ok'}
            except Exception as e:
                result = {'result':'error', 'error': str(e)}
        else:
            result = {'result':'error', 'error': 'Datos insuficientes'}
        return result


# @class_declaration post #
class post(trainB_post):
    pass
