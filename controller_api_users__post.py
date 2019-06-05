from django.core import serializers
from models.fltrainb.user import user as User
import json

class interna_post():
    pass


# @class_declaration trainB_post #
class trainB_post(interna_post):

    @staticmethod
    def start(pk, data):

       # print(data.__name__)
        if  'email' in data:
            try:
                if "iduser" in data:
                     User().load({"iduser":data['iduser']}).update(data)
                else:
                    User().create(data)
                result = '{"result":"ok"}'
            except  Exception as e:
                result = '{"result":"error en los datos"}'
                print(str(e))
        else:
            result = '{"result":"error"}'
        return json.loads(result)


# @class_declaration post #
class post(trainB_post):
    pass
