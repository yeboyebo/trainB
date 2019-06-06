from django.core import serializers
from models.fltrainb.company import company as Company
import json

class interna_post():
    pass


# @class_declaration trainB_post #
class trainB_post(interna_post):

    @staticmethod
    def start(request):
        data = request.data
        print(data)
        if  'nif' in data:
            try:
                Company().create(data)
                result = {'result':'ok'}
            except Exception as e:
                result = {'result':'error', 'error': str(e)}
        else:
            result = {'result':'error', 'error': 'Datos insuficientes'}
        return result


# @class_declaration post #
class post(trainB_post):
    pass
