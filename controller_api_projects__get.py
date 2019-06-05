from models.fltrainb.project import project as Project
from controllers.api.trainB.projects.serializers.project_serializer import projectSerializer as Serializer
import json
from django.http import HttpResponse

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
            project = Project().load({'idproject':pk})
            result = serializador.serialize(project)
            print(project.get_fields()[3].verbose_name.title())
            print(project.get_fields()[3].get_internal_type())

        else:
            projects = Project().get_collection()
            result = []
            for project in projects:
                result.append(serializador.serialize(project))
        return HttpResponse(json.dumps(result), status=200, content_type="application/json")


# @class_declaration get #
class get(trainB_get):
    pass
