from django.core import serializers
from models.fltrainb.comment import comment as Comment
import json

class interna_postComments():
    pass


# @class_declaration trainB_post #
class trainB_postComments(interna_postComments):

    @staticmethod
    def start(pk, data):
        if  'task' in data and 'user' in data and 'description' in data:
            try:
                if 'idcomment' in data:
                    Comment().load({"idcomment":data['idcomment']}).update(data)
                else:
                    print("Voy a crear el comentario")
                    Comment().create(data)
                result = {'result':'ok'}
            except Exception as e:
                result = {'result':'error', 'error': str(e)}
        else:
            result = {'result':'error', 'error': 'Datos insuficientes'}
        return result


# @class_declaration post #
class postComments(trainB_postComments):
    pass
