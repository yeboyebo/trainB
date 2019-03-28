from django.core import serializers
from models.fltrainb.consultant import consultant as Consultant
from controllers.api.trainB.users.serializers.consultant_serializer import consultantSerializer as Serializer
import json

class interna_getConsultant():
    pass


# @class_declaration trainB_getConsultant #
class trainB_getConsultant(interna_getConsultant):

    @staticmethod
    def start(pk, data):

        serializador = Serializer()
        if  'idconsultant' in data:
            user = Consultant().load(data)
            result = serializador.serialize(user)
        else:
            users = Consultant().get_collection()
            result = []
            for user in users:
                result.append(serializador.serialize(user))
        return result


# @class_declaration getConsultant #
class getConsultant(trainB_getConsultant):
    pass
