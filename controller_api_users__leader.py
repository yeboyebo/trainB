from django.core import serializers
from models.fltrainb.leader import leader as Leader
import json

class interna_leader():
    pass


# @class_declaration trainB_leader #
class trainB_leader(interna_leader):

    @staticmethod
    def start(pk, data):
        
       # print(data.__name__)
        if  'email' in data:
            try:
                Leader().create(data)
                result = '{"result":"ok"}'
            except  Exception as e:
                result = '{"result":"error en los datos"}'
                print(str(e))
        else:
            result = '{"result":"error"}'
        return json.loads(result)


# @class_declaration leader #
class leader(trainB_leader):
    pass
