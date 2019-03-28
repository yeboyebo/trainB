from collections import OrderedDict
from controllers.api.trainB.users.serializers.user_serializer import userSerializer as UserSerializer

class interna_projectSerializer():
    pass


# @class_declaration trainB_projectSerializer #
class trainB_projectSerializer(interna_projectSerializer):

    @staticmethod
    def serialize(projects):
        user = UserSerializer()
        data = OrderedDict()

        for project in projects:
            data.update({
                'name': project.get_data('name'),
                'description': project.get_data('description'),
                'budget': project.get_data('budget'),
                'cost': project.get_data('cost'),
                'leader':project.get_data('leader').get_name()
            })

        return data


# @class_declaration projectSerializer #
class projectSerializer(trainB_projectSerializer):
    pass
