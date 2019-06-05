from models.fltrainb.task import task as Task
from controllers.api.trainB.projects.serializers.task_serializer import taskSerializer as Serializer

class interna_getTasks():
    pass


# @class_declaration trainB_get #q
class trainB_getTasks(interna_getTasks):

    @staticmethod
    def start(pk, data):

        serializador = Serializer()
        if  'idtask' in data:
            result = serializador.serialize(Task().load(data))
        elif pk:
            result = serializador.serialize(Task().load({'idtask':pk}))
        else:
            tasks = Task().get_collection()
            result = []
            for task in tasks:
                result.append(serializador.serialize(task))
        return result


# @class_declaration get #
class getTasks(trainB_getTasks):
    pass
