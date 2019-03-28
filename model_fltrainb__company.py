# @class_declaration interna_company #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.address import address as Address


class interna_company(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_company #
class trainb_company(interna_company):

    idcompany = baseraw.AutoField(
        db_column="idcompany",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )._miextend(
        REQUIRED=True,
        OLDTIPO="SERIAL",
        visiblegrid=False,
    )
    name = baseraw.CharField(
        db_column="name",
        verbose_name=FLUtil.translate(u"Nombre de la empresa", u"MetaData"),
        blank=False,
        null=False,
        max_length=100
    )._miextend(
        OLDTIPO="STRING"
    )
    nif = baseraw.CharField(
        db_column="nif",
        verbose_name=FLUtil.translate(u"NIF", u"MetaData"),
        blank=False,
        null=False,
        max_length=20,
        unique=True
    )._miextend(
        OLDTIPO="STRING"
    )
    email = baseraw.CharField(
        db_column="email",
        verbose_name=FLUtil.translate(u"Email", u"MetaData"),
        blank=False,
        null=True,
        max_length=150
    )._miextend(
        OLDTIPO="STRING"
    )
    phone = baseraw.CharField(
        db_column="phone",
        verbose_name=FLUtil.translate(u"Teléfono", u"MetaData"),
        blank=False,
        null=True,
        max_length=20
    )._miextend(
        OLDTIPO="STRING"
    )
    address = baseraw.ForeignKey(
        "address",
        db_column="address",
        verbose_name=FLUtil.translate(u"Dirección", u"MetaData"),
        blank=False,
        null=False,
        to_field="idaddress",
        on_delete=baseraw.CASCADE,
        related_name="company_address__fk__address_idaddress"
    )._miextend(
            OLDTIPO="SERIAL"
    )

    def getName(self):
        return self.name

    def create(self, data):
        data['address'] = Address().load(data['address'])
        return super().create(data)

    def get_address(self):
        return self.address

    class Meta:
        abstract = True


# @class_declaration company #
class company(trainb_company):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Empresas", u"MetaData")
        db_table = u"company"
