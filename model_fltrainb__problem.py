# @class_declaration interna_problem #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.improvement import improvement as Improvement


class interna_problem(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_problem #
class trainb_problem(interna_problem):

    idproblem = baseraw.AutoField(
        db_column="idproblem",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )

    description = baseraw.TextField(
        db_column="description",
        verbose_name=FLUtil.translate(u"Descripción", u"MetaData"),
        blank=False,
        null=False
    )

    improvement = baseraw.ForeignKey(
        "improvement",
        db_column="improvement",
        verbose_name=FLUtil.translate(u"Mejora", u"MetaData"),
        blank=False,
        null=False,
        to_field="idimprovement",
        on_delete=baseraw.PROTECT,
        related_name="problems"
    )

    class Meta:
        abstract = True


# @class_declaration problem #
class problem(trainb_problem):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Problemas", u"MetaData")
        db_table = u"problem"
