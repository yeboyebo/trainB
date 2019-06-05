# @class_declaration interna_action #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.improvement import improvement as Improvement


class interna_action(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_action #
class trainb_action(interna_action):

    idaction = baseraw.AutoField(
        db_column="idaction",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )

    description = baseraw.TextField(
        db_column="description",
        verbose_name=FLUtil.translate(u"Descripción", u"MetaData"),
        blank=False,
        null=False
    )

    state = baseraw.CharField(
        db_column="state",
        verbose_name=FLUtil.translate(u"Estado", u"MetaData"),
        blank=False,
        null=False,
        max_length=100,
        unique=False
    )

    improvement = baseraw.ForeignKey(
        "improvement",
        db_column="improvement",
        verbose_name=FLUtil.translate(u"Mejora", u"MetaData"),
        blank=False,
        null=False,
        to_field="idimprovement",
        on_delete=baseraw.PROTECT,
        related_name="actions"
    )

    class Meta:
        abstract = True


# @class_declaration action #
class action(trainb_action):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Acciones", u"MetaData")
        db_table = u"action"
