from collections import OrderedDict
from controllers.api.trainB.users.serializers.user_serializer import userSerializer as UserSerializer

class interna_improvmentSerializer():
    pass


# @class_declaration trainB_improvmentSerializer #
class trainB_improvmentSerializer(interna_improvmentSerializer):

    @staticmethod
    def serialize(improvment):
        user = UserSerializer()
        data = OrderedDict({
            'name': improvment.get_data('name'),
            'description': improvment.get_data('description'),
            'budget': improvment.get_data('budget'),
            'cost': improvment.get_data('cost'),
            'leader': user.serialize(improvment.get_data('leader')),
            'consultant': user.serialize(improvment.get_data('consultant'))
        })
        return data


# @class_declaration improvmentSerializer #
class improvmentSerializer(trainB_improvmentSerializer):
    pass
