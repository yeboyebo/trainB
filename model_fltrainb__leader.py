# @class_declaration interna_leader #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.user import user as User


class interna_leader(User):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_leader #
class trainb_leader(interna_leader):

    idleader = baseraw.AutoField(
        db_column="idleader",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )._miextend(
        REQUIRED=True,
        OLDTIPO="SERIAL",
        visiblegrid=False,
    )

    class Meta:
        abstract = True


# @class_declaration leader #
class leader(trainb_leader):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Líderes del cambio", u"MetaData")
        db_table = u"leader"
