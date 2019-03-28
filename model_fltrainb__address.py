# @class_declaration interna_address #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw


class interna_address(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_address #
class trainb_address(interna_address):

    idaddress = baseraw.AutoField(
        db_column="idaddress",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )._miextend(
        REQUIRED=True,
        OLDTIPO="SERIAL",
        visiblegrid=False,
    )
    description = baseraw.CharField(
        db_column="description",
        verbose_name=FLUtil.translate(u"Descripcion", u"MetaData"),
        blank=False,
        null=False,
        max_length=140
    )._miextend(
        OLDTIPO="STRING"
    )
    street_address = baseraw.CharField(
        db_column="street_address",
        verbose_name=FLUtil.translate(u"Dirección", u"MetaData"),
        blank=False,
        null=False,
        max_length=100
    )._miextend(
        OLDTIPO="STRING"
    )
    city = baseraw.CharField(
        db_column="city",
        verbose_name=FLUtil.translate(u"Ciudad", u"MetaData"),
        blank=False,
        null=False,
        max_length=100
    )._miextend(
        OLDTIPO="STRING"
    )
    country = baseraw.CharField(
        db_column="country",
        verbose_name=FLUtil.translate(u"País", u"MetaData"),
        blank=False,
        null=False,
        max_length=100
    )._miextend(
        OLDTIPO="STRING"
    )
    postal_code = baseraw.CharField(
        db_column="postal_code",
        verbose_name=FLUtil.translate(u"Código postal", u"MetaData"),
        blank=False,
        null=False,
        max_length=10
    )._miextend(
        OLDTIPO="STRING"
    )

    def getName(self):
        return self.name

    class Meta:
        abstract = True


# @class_declaration address #
class address(trainb_address):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Direcciones", u"MetaData")
        db_table = u"address"
