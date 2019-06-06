from collections import OrderedDict
from controllers.api.trainB.companies.serializers.company_serializer import companySerializer as CompanySerializer

class interna_userSerializer():
    pass


# @class_declaration trainB_userSerializer #
class trainB_userSerializer(interna_userSerializer):

    @staticmethod
    def serialize(user):
        company = CompanySerializer()
        data = OrderedDict({
            'name': user.name,
            'surname': user.surname,
            'email': user.email,
            'phone': user.phone,
            'rol': user.rol,
            'company': company.serialize(user.get_company())
        })
        return data


# @class_declaration userSerializer #
class userSerializer(trainB_userSerializer):
    pass
