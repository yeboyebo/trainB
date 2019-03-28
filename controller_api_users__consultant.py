from django.core import serializers
from models.fltrainb.consultant import consultant as Consultant
import json

class interna_consultant():
    pass


# @class_declaration trainB_consultant #
class trainB_consultant(interna_consultant):

    @staticmethod
    def start(pk, data):
        
       # print(data.__name__)
        if  'email' in data:
            try:
                Consultant().create(data)
                result = '{"result":"ok"}'
            except  Exception as e:
                result = '{"result":"error en los datos"}'
                print(str(e))
        else:
            result = '{"result":"error"}'
        return json.loads(result)


# @class_declaration consultant #
class consultant(trainB_consultant):
    pass
