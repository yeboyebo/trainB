from collections import OrderedDict
from controllers.api.trainB.users.serializers.user_serializer import userSerializer as UserSerializer
from controllers.api.trainB.projects.serializers.task_serializer import taskSerializer as TaskSerializer
from controllers.api.trainB.projects.serializers.improvement_serializer import improvementSerializer as ImprovementSerializer

class interna_sprintSerializer():
    pass

# @class_declaration trainB_sprintSerializer #
class trainB_sprintSerializer(interna_sprintSerializer):

    @staticmethod
    def serialize(sprint):
        improvementSerializer = ImprovementSerializer()
        data = OrderedDict({
            'name': sprint.get_data('name'),
            'description': sprint.get_data('description'),
            'cost': sprint.get_data('cost'),
            'state': sprint.get_data('state'),
            'objective': sprint.get_data('objective'),
            'improvement': improvementSerializer.serialize(sprint.get_improvement()),
            'action': sprint.get_action().get_data('description'),
            'users': sprintSerializer.serialize_users(sprint.get_users()),
            'tasks': sprintSerializer.serialize_tasks(sprint.get_tasks())
        })
        return data

    @staticmethod
    def serialize_users(users):
        users = []
        serializer = UserSerializer()
        for user in users:
            users.append(serializer.serialize(user))
        return users

    @staticmethod
    def serialize_tasks(users):
        tasks = []
        serializer = TaskSerializer()
        for task in tasks:
            tasks.append(serializer.serialize(task))
        return tasks

# @class_declaration sprintSerializer #
class sprintSerializer(trainB_sprintSerializer):
    pass
