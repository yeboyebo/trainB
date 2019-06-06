from collections import OrderedDict

class interna_addressSerializer():
    pass


# @class_declaration trainB_addressSerializer #
class trainB_addressSerializer(interna_addressSerializer):

    @staticmethod
    def serialize(company):

        data = OrderedDict({
            'description': company.get_data('description'),
            'street': company.get_data('street_address'),
            'city': company.get_data('city'),
            'postcode': company.get_data('postal_code'),
            'country': company.get_data('country')
        })
        return  data


# @class_declaration addressSerializer #
class addressSerializer(trainB_addressSerializer):
    pass
