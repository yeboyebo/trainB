# @class_declaration interna_improvement #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.company import company as Company


class interna_improvement(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_improvement #
class trainb_improvement(interna_improvement):

    idimprovement = baseraw.AutoField(
        db_column="idimprovement",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )
    objective = baseraw.TextField(
        db_column="objective",
        verbose_name=FLUtil.translate(u"Objetivo", u"MetaData"),
        blank=True,
        null=True
    )
    cost = baseraw.FloatField(
        db_column="cost",
        verbose_name=FLUtil.translate(u"Coste", u"MetaData"),
        blank=True,
        null=True,
        default=None
    )
    priority = baseraw.IntField(
        db_column="priority",
        verbose_name=FLUtil.translate(u"Prioridad", u"MetaData"),
        blank=False,
        null=False,
        default=0
    )



    class Meta:
        abstract = True


# @class_declaration improvement #
class improvement(trainb_improvement):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Usuarios", u"MetaData")
        db_table = u"improvement"
