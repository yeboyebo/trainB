from collections import OrderedDict
from controllers.api.trainB.companies.serializers.address_serializer import addressSerializer as AddressSerializer

class interna_companySerializer():
    pass


# @class_declaration trainB_companySerializer #
class trainB_companySerializer(interna_companySerializer):

    @staticmethod
    def serialize(company):
        address = AddressSerializer()
        data = OrderedDict({
            'name': company.get_data('name'),
            'nif': company.get_data('nif'),
            'email': company.get_data('email'),
            'phone': company.get_data('phone'),
            'address': address.serialize(company.get_data('address'))
        })
        return data


# @class_declaration companySerializer #
class companySerializer(trainB_companySerializer):
    pass
