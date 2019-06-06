from collections import OrderedDict
# from controllers.api.trainB.users.serializers.user_serializer import userSerializer as UserSerializer

class interna_improvementSerializer():
    pass


# @class_declaration trainB_improvementSerializer #
class trainB_improvementSerializer(interna_improvementSerializer):

    @staticmethod
    def serialize(improvement):
        data = OrderedDict({
            'objetive': improvement.get_data('objective'),
            'cost': improvement.get_data('cost'),
            'problems': improvementSerializer.serialize_problems(improvement.get_problems()),
            'actions': improvementSerializer.serialize_actions(improvement.get_actions()),
        })
        return data

    @staticmethod
    def serialize_problems(data):
        problems = []

        for p in data:
            problems.append(p.get_data('description'))
        return problems

    @staticmethod
    def serialize_actions(data):
        problems = []

        for p in data:
            problems.append(p.get_data('description'))
        return problems


# @class_declaration improvementSerializer #
class improvementSerializer(trainB_improvementSerializer):
    pass
