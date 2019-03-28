# @class_declaration interna_user #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.company import company as Company


class interna_user(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_user #
class trainb_user(interna_user):

    iduser = baseraw.AutoField(
        db_column="iduser",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )._miextend(
        REQUIRED=True,
        OLDTIPO="SERIAL",
        visiblegrid=False,
    )
    email = baseraw.CharField(
        db_column="email",
        verbose_name=FLUtil.translate(u"E-mail", u"MetaData"),
        blank=False,
        null=False,
        max_length=100,
        unique=True
    )._miextend(
        OLDTIPO="STRING"
    )
    password = baseraw.CharField(
        db_column="password",
        verbose_name=FLUtil.translate(u"Contraseña", u"MetaData"),
        blank=False,
        null=False,
        max_length=50
    )._miextend(
        OLDTIPO="STRING"
    )
    name = baseraw.CharField(
        db_column="name",
        verbose_name=FLUtil.translate(u"Nombre", u"MetaData"),
        blank=False,
        null=False,
        max_length=100
    )._miextend(
        OLDTIPO="STRING"
    )
    surname = baseraw.CharField(
        db_column="surname",
        verbose_name=FLUtil.translate(u"Apellidos", u"MetaData"),
        blank=False,
        null=False,
        max_length=150
    )._miextend(
        OLDTIPO="STRING"
    )
    birtday = baseraw.CharField(
        db_column="birtday",
        verbose_name=FLUtil.translate(u"Fecha Nacimiento", u"MetaData"),
        blank=True,
        null=True,
        max_length=10
    )._miextend(
        OLDTIPO="DATE"
    )
    rol = baseraw.CharField(
        db_column="rol",
        verbose_name=FLUtil.translate(u"Rol", u"MetaData"),
        blank=False,
        null=False,
        max_length=20
    )._miextend(
        optionslist=u",Consultor,Developer,Líder del cambio,Receptor del cambio",
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
    company = baseraw.ForeignKey(
        "company",
        db_column="company",
        verbose_name=FLUtil.translate(u"Empresa", u"MetaData"),
        blank=False,
        null=False,
        max_length=30,
        to_field="idcompany",
        on_delete=baseraw.CASCADE,
        related_name="user_company__fk__company_idcompany"
    )._miextend(
            OLDTIPO="SERIAL"
    )

    def create(self, data):
        print("Creo company")
        data['company'] = Company().load(data['company'])
        print("super")
        return super().create(data)

    def get_name(self):
        return self.name + " " + self.surname

    def get_company(self):
        return self.company

    class Meta:
        abstract = True


# @class_declaration user #
class user(trainb_user):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Usuarios", u"MetaData")
        db_table = u"user"
