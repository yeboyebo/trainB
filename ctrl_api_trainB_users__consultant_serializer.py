from collections import OrderedDict
from controllers.api.trainB.companies.serializers.company_serializer import companySerializer as CompanySerializer
from controllers.api.trainB.users.serializers.project_serializer import projectSerializer as ProjectSerializer

class interna_consultantSerializer():
    pass


# @class_declaration trainB_consultantSerializer #
class trainB_consultantSerializer(interna_consultantSerializer):

    @staticmethod
    def serialize(consultant):
        company = CompanySerializer()
        project = ProjectSerializer()
        data = OrderedDict({
            'name': consultant.name,
            'surname': consultant.surname,
            'email': consultant.email,
            'phone': consultant.phone,
            'rol': consultant.rol,
            'company':  consultant.get_company().get_data('name'),
            'projects': project.serialize(consultant.get_projects())
        })
        return data


# @class_declaration consultantSerializer #
class consultantSerializer(trainB_consultantSerializer):
    pass
