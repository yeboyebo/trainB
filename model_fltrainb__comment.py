# @class_declaration interna_comment #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.task import task as Task
from models.fltrainb.user import user as User
from datetime import datetime

class interna_comment(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_comment #
class trainb_comment(interna_comment):

    idcomment = baseraw.AutoField(
        db_column="idcomment",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )._miextend(
        REQUIRED=True,
        OLDTIPO="SERIAL",
        visiblegrid=False,
    )
    description = baseraw.TextField(
        db_column="description",
        verbose_name=FLUtil.translate(u"Descripcion", u"MetaData"),
        blank=False,
        null=True,
    )
    date = baseraw.DateTimeField(
        db_column="date",
        verbose_name=FLUtil.translate(u"Fecha y hora", u"MetaData"),
        blank=True,
        default=datetime.now
    )
    task = baseraw.ForeignKey(
        "task",
        db_column="idtask",
        verbose_name=FLUtil.translate(u"Tarea", u"MetaData"),
        blank=False,
        null=False,
        max_length=30,
        to_field="idtask",
        on_delete=baseraw.PROTECT,
        related_name="comments"
    )
    user = baseraw.ForeignKey(
        "user",
        db_column="iduser",
        verbose_name=FLUtil.translate(u"Líder del cambio", u"MetaData"),
        blank=False,
        null=False,
        max_length=30,
        to_field="iduser",
        on_delete=baseraw.PROTECT,
        related_name="user"
    )

    def create(self, data):
        data["task"] = Task().load({"idtask":data["task"]})
        data["user"] = User().load({"iduser":data["user"]})
        return super().create(data)

    def update(self, data):
        if "task" in data:
            del data["task"]
        if "user" in data:
            del data["user"]
        return super().update(data)

    def get_projects(self):
        return self.projects.all()

    class Meta:
        abstract = True


# @class_declaration comment #
class comment(trainb_comment):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Consultores", u"MetaData")
        db_table = u"comment"
