# @class_declaration interna_project #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.consultant import consultant as Consultant
from models.fltrainb.leader import leader as Leader

class interna_project(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_project #
class trainb_project(interna_project):

    idproject = baseraw.AutoField(
        db_column="idproject",
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

    budget = baseraw.CharField(
        db_column="budget",
        verbose_name=FLUtil.translate(u"Presupuesto", u"MetaData"),
        blank=False,
        null=True,
        max_length=12
    )._miextend(
        OLDTIPO="STRING"
    )

    cost = baseraw.CharField(
        db_column="cost",
        verbose_name=FLUtil.translate(u"Coste", u"MetaData"),
        blank=False,
        null=True,
        max_length=12
    )._miextend(
        OLDTIPO="STRING"
    )

    start_date = baseraw.DateField(
        db_column="start_date",
        verbose_name=FLUtil.translate(u"Fecha de comienzo", u"MetaData"),
        blank=True,
        null=True
    )._miextend(
        OLDTIPO="DATE"
    )

    finish_date = baseraw.DateField(
        db_column="finish_date",
        verbose_name=FLUtil.translate(u"Fecha de finalización", u"MetaData"),
        blank=True,
        null=True
    )._miextend(
        OLDTIPO="DATE"
    )

    leader = baseraw.ForeignKey(
        "leader",
        db_column="leader",
        verbose_name=FLUtil.translate(u"Líder del cambio", u"MetaData"),
        blank=False,
        null=False,
        max_length=30,
        to_field="idleader",
        on_delete=baseraw.PROTECT,
        related_name="project_leader__fk__leader_idleader"
    )._miextend(
        OLDTIPO="SERIAL"
    )

    consultant = baseraw.ForeignKey(
        "consultant",
        db_column="consultant",
        verbose_name=FLUtil.translate(u"Consultor", u"MetaData"),
        blank=False,
        null=False,
        max_length=30,
        to_field="idconsultant",
        on_delete=baseraw.PROTECT,
        related_name="projects"
    )._miextend(
        OLDTIPO="SERIAL"
    )

    def create(self, data):
        data['leader'] = Leader().load(data['leader'])
        data['consultant'] = Consultant().load(data['consultant'])
        return super().create(data)

    def update(self, data):
        data['leader'] = Leader().load(data['leader'])
        data['consultant'] = Consultant().load(data['consultant'])
        return super().update(data)

    class Meta:
        abstract = True


# @class_declaration project #
class project(trainb_project):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Proyectos", u"MetaData")
        db_table = u"project"
