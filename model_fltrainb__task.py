# @class_declaration interna_task #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.user import user as User
from models.fltrainb.sprint import sprint as Sprint

class interna_task(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_task #
class trainb_task(interna_task):

    idtask = baseraw.AutoField(
        db_column="idtask",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )._miextend(
        REQUIRED=True,
        OLDTIPO="SERIAL",
        visiblegrid=False,
    )
    name = baseraw.CharField(
        db_column="name",
        verbose_name=FLUtil.translate(u"Nombre", u"MetaData"),
        blank=False,
        null=False,
        max_length=200
    )._miextend(
        OLDTIPO="STRING"
    )
    description = baseraw.TextField(
        db_column="description",
        verbose_name=FLUtil.translate(u"Descripcion", u"MetaData"),
        blank=False,
        null=True,
    )._miextend(
        OLDTIPO="STRING"
    )
    cost = baseraw.CharField(
        db_column="cost",
        verbose_name=FLUtil.translate(u"Coste", u"MetaData"),
        blank=True,
        null=True,
        max_length=12,
        default=0
    )._miextend(
        OLDTIPO="STRING"
    )
    finish_date = baseraw.DateField(
        db_column="finish_date",
        verbose_name=FLUtil.translate(u"Fecha de comienzo", u"MetaData"),
        blank=True,
        null=True
    )._miextend(
        OLDTIPO="DATE"
    )
    order = baseraw.IntegerField(
        db_column="order",
        verbose_name=FLUtil.translate(u"Orden", u"MetaData"),
        blank=False,
        null=False,
        default=0
    )._miextend(
        OLDTIPO="STRING"
    )
    sprint = baseraw.ForeignKey(
        "sprint",
        db_column="idsprint",
        verbose_name=FLUtil.translate(u"Líder del cambio", u"MetaData"),
        blank=False,
        null=False,
        max_length=30,
        to_field="idsprint",
        on_delete=baseraw.PROTECT,
        related_name="tasks"
    )._miextend(
        OLDTIPO="SERIAL"
    )
    responsable = baseraw.ForeignKey(
        "user",
        db_column="idresponsable",
        verbose_name=FLUtil.translate(u"Responsable", u"MetaData"),
        blank=True,
        null=True,
        max_length=30,
        to_field="iduser",
        on_delete=baseraw.PROTECT,
        related_name="responsable"
    )._miextend(
        OLDTIPO="SERIAL"
    )

    def create(self, data):
        data["sprint"] = Sprint().load({"idsprint":data["sprint"]})
        data["responsable"] = User().load({"iduser":data["responsable"]})
        return super().create(data)

    def update(self, data):
        data["sprint"] = Sprint().load({"idsprint":data["sprint"]})
        data["responsable"] = User().load({"iduser":data["responsable"]})
        return super().update(data)

    def get_user(self):
        return self.users.all()

    def get_comments(self):
        return self.comments.all()

    class Meta:
        abstract = True


# @class_declaration task #
class task(trainb_task):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Tareas", u"MetaData")
        db_table = u"task"
