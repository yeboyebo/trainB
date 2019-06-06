from collections import OrderedDict
from controllers.api.trainB.users.serializers.user_serializer import userSerializer as UserSerializer

class interna_projectSerializer():
    pass


# @class_declaration trainB_projectSerializer #
class trainB_projectSerializer(interna_projectSerializer):

    @staticmethod
    def serialize(project):
        user = UserSerializer()
        data = OrderedDict({
            'name': project.get_data('name'),
            'description': project.get_data('description'),
            'budget': project.get_data('budget'),
            'cost': project.get_data('cost'),
            'leader': user.serialize(project.get_data('leader')),
            'consultant': user.serialize(project.get_data('consultant'))
        })
        return data


# @class_declaration projectSerializer #
class projectSerializer(trainB_projectSerializer):
    pass
