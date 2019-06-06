from collections import OrderedDict
from controllers.api.trainB.users.serializers.user_short_serializer import userShortSerializer as UserSerializer

class interna_taskSerializer():
    pass


# @class_declaration trainB_taskSerializer #
class trainB_taskSerializer(interna_taskSerializer):

    @staticmethod
    def serialize(task):
        user = UserSerializer()
        print("Serializo task")
        data = OrderedDict({
            'idtask': task.get_data('idtask'),
            'name': task.get_data('name'),
            'description': task.get_data('description'),
            'cost': task.get_data('cost'),
            'responsable': user.serialize(task.get_data('responsable')),
            'finish_date': task.get_data('finish_date'),
            'order': task.get_data('order'),
            'comments': taskSerializer.serializeComments(task.get_comments())
        })
        return data

    @staticmethod
    def serializeComments(comments):
        data = []
        user = UserSerializer()
        for comment in comments:
            data.append(OrderedDict({
                'user': user.serialize(comment.get_data('user')),
                'description': comment.get_data('description')
            }))
        return data

# @class_declaration taskSerializer #
class taskSerializer(trainB_taskSerializer):
    pass
