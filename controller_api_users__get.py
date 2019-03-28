from django.core import serializers
from models.fltrainb.user import user as User
from controllers.api.trainB.users.serializers.user_serializer import userSerializer as Serializer
import json

class interna_get():
    pass


# @class_declaration trainB_get #
class trainB_get(interna_get):

    @staticmethod
    def start(pk, data):

        serializador = Serializer()
        if  'iduser' in data:
            user = User().load(data)
            result = serializador.serialize(user)
        else:
            users = User().get_collection()
            result = []
            for user in users:
                result.append(serializador.serialize(user))
        return result


# @class_declaration get #
class get(trainB_get):
    pass
