from models.fltrainb.improvement import improvement as Improvement
from controllers.api.trainB.improvements.serializers.improvement_serializer import improvementSerializer as Serializer

class interna_getImprovements():
    pass


# @class_declaration trainB_get #q
class trainB_getImprovements(interna_getImprovements):

    @staticmethod
    def start(pk, data):

        serializador = Serializer()
        if  'idimprovement' in data:
            result = serializador.serialize(Improvement().load(data))
        elif pk:
            result = serializador.serialize(Improvement().load({'idimprovement':pk}))
        else:
            improvements = Improvement().get_collection()
            result = []
            for improvement in improvements:
                result.append(serializador.serialize(improvement))
        return result


# @class_declaration get #
class getImprovements(trainB_getImprovements):
    pass
