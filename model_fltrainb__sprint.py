# @class_declaration interna_sprint #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.project import project as Project
from models.fltrainb.improvement import improvement as Improvement
from models.fltrainb.action import action as Action
from models.fltrainb.user import user as User

class interna_sprint(baseraw.RawModel):
    pass

    class Meta:
        abstract = True


# @class_declaration trainb_sprint #
class trainb_sprint(interna_sprint):

    idsprint = baseraw.AutoField(
        db_column="idsprint",
        verbose_name=FLUtil.translate(u"Identificador", u"MetaData"),
        primary_key=True
    )
    objective = baseraw.TextField(
        db_column="objective",
        verbose_name=FLUtil.translate(u"Definición de hecho", u"MetaData"),
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
    start_date = baseraw.DateField(
        db_column="start_date",
        verbose_name=FLUtil.translate(u"Fecha de inicio", u"MetaData"),
        blank=True,
        null=True
    )
    finish_date = baseraw.DateField(
        db_column="finish_date",
        verbose_name=FLUtil.translate(u"Fecha de fin", u"MetaData"),
        blank=True,
        null=True
    )
    state = baseraw.CharField(
        db_column="state",
        verbose_name=FLUtil.translate(u"Estado", u"MetaData"),
        blank=False,
        null=False,
        default="Propuesta",
        max_length=30
    )._miextend(
        optionslist=u",Propuesta,Rechazado,Aceptado",
        OLDTIPO="STRING"
    )
    project = baseraw.ForeignKey(
        "project",
        db_column="idproject",
        verbose_name=FLUtil.translate(u"Proyecto", u"MetaData"),
        blank=False,
        null=False,
        to_field="idproject",
        on_delete=baseraw.PROTECT,
        related_name="sprints"
    )
    improvement = baseraw.ForeignKey(
        "improvement",
        db_column="idimprovement",
        verbose_name=FLUtil.translate(u"Mejora", u"MetaData"),
        blank=False,
        null=False,
        to_field="idimprovement",
        on_delete=baseraw.PROTECT,
        related_name="improvements"
    )
    action = baseraw.ForeignKey(
        "action",
        db_column="idaction",
        verbose_name=FLUtil.translate(u"Acción", u"MetaData"),
        blank=False,
        null=False,
        to_field="idaction",
        on_delete=baseraw.PROTECT,
        related_name="actions"
    )
    users = baseraw.ManyToManyField(User)

    def create(self, data):
        data['project'] = Project().load({'idproject':data['project']})
        data['improvement'] = Improvement().load({'idimprovement':data['improvement']})
        data['action'] = Action().load({'idaction':data['action']})
        users = data['users']
        del data['users']
        sprint = super().create(data)
        sprint.add_users(users)
        return sprint

    def update(self, data):
        if "project" in data:
            del data['project']
        if "users" in data:
            del data['users']
        data['improvement'] = Improvement().load({'idimprovement':data['improvement']})
        data['action'] = Action().load({'idaction':data['action']})
        return super().update(data)

    def get_improvements(self):
        return self.improvements.all()

    def get_action(self):
        return self.action.all()

    def get_users(self):
        return self.users.all()

    def get_tasks(self):
        return self.tasks.all()

    def add_users(self, users):
        for idUser in users:
            self.users.add(User().load(idUser))

    class Meta:
        abstract = True


# @class_declaration sprint #
class sprint(trainb_sprint):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Usuarios", u"MetaData")
        db_table = u"sprint"
