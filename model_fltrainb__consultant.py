# @class_declaration interna_consultant #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.user import user as User
# from models.fltrainb.project import project as Project

class interna_consultant(User):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_consultant #
class trainb_consultant(interna_consultant):

    idconsultant = baseraw.AutoField(
        db_column="idconsultant",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )._miextend(
        REQUIRED=True,
        OLDTIPO="SERIAL",
        visiblegrid=False,
    )

    # projects = []

    # def __init__(self):
    #    self.projects = project.objects.get(idconsultant=self.idconsultant)

    def get_projects(self):
        return self.projects.all()

    class Meta:
        abstract = True


# @class_declaration consultant #
class consultant(trainb_consultant):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Consultores", u"MetaData")
        db_table = u"consultant"
