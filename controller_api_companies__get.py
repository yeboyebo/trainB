from models.fltrainb.company import company as Company
from controllers.api.trainB.companies.serializers.company_serializer import companySerializer as Serializer

class interna_get():
    pass


# @class_declaration trainB_get #q
class trainB_get(interna_get):

    @staticmethod
    def start(pk, data):
        
        serializador = Serializer()
        if  'idcompany' in data:
            result = serializador.serialize(Company().load(data))
        elif pk:
            result = serializador.serialize(Company().load({'idcompany':pk}))
        else:
            companies = Company().get_collection()
            result = []
            for company in companies:
                result.append(serializador.serialize(company))
        return result


# @class_declaration get #
class get(trainB_get):
    pass
