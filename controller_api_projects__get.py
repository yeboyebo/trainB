from models.fltrainb.project import project as Project
from controllers.api.trainB.projects.serializers.project_serializer import projectSerializer as Serializer

class interna_get():
    pass


# @class_declaration trainB_get #q
class trainB_get(interna_get):

    @staticmethod
    def start(pk, data):

        serializador = Serializer()
        if  'idproject' in data:
            result = serializador.serialize(Project().load(data))
        elif pk:
            result = serializador.serialize(Project().load({'idproject':pk}))
        else:
            projects = Project().get_collection()
            result = []
            for project in projects:
                result.append(serializador.serialize(project))
        return result


# @class_declaration get #
class get(trainB_get):
    pass
