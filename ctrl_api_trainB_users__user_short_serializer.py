from collections import OrderedDict

class interna_userShortSerializer():
    pass


# @class_declaration trainB_userShortSerializer #
class trainB_userShortSerializer(interna_userShortSerializer):

    @staticmethod
    def serialize(user):

        data = OrderedDict({
            'name': user.get_name(),
            'email': user.get_data('email'),
            'phone': user.get_data('phone'),
            'rol': user.get_data('rol')
        })
        return data


# @class_declaration userShortSerializer #
class userShortSerializer(trainB_userShortSerializer):
    pass
