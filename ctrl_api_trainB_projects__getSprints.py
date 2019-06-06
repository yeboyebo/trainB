from models.fltrainb.sprint import sprint as Sprint
from controllers.api.trainB.projects.serializers.sprint_serializer import sprintSerializer as Serializer

class interna_getSprints():
    pass


# @class_declaration trainB_get #q
class trainB_getSprints(interna_getSprints):

    @staticmethod
    def start(pk, data):

        serializador = Serializer()
        if  'idSprint' in data:
            result = serializador.serialize(Sprint().load(data))
        elif pk:
            result = serializador.serialize(Sprint().load({'idsprint':pk}))
        else:
            sprints = Sprint().get_collection()
            result = []
            for sprint in sprints:
                result.append(serializador.serialize(sprint))
        return result


# @class_declaration get #
class getSprints(trainB_getSprints):
    pass
