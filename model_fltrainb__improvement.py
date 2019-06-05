# @class_declaration interna_improvement #
from YBLEGACY.FLUtil import FLUtil
from YBLEGACY import baseraw
from models.fltrainb.project import project as Project



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
    priority = baseraw.IntegerField(
        db_column="priority",
        verbose_name=FLUtil.translate(u"Prioridad", u"MetaData"),
        blank=False,
        null=False,
        default=0
    )
    state = baseraw.CharField(
        db_column="state",
        verbose_name=FLUtil.translate(u"Estado", u"MetaData"),
        blank=False,
        null=False,
        default="Propuesta",
        max_length=30
    )._miextend(
         optionslist=u",Propuesta,Rechazada,Pendiente,En ejecución,En ejecución En medicion, En medicion finalizando, Finalizado",
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
        related_name="project"
    )

    def create(self, data):
        data['project'] = Project().load({'idproject':data['project']})
        problems = data['problems']
        actions = data['actions']
        # Limpio data para crear con sus campos unicamente
        del data['problems']
        del data['actions']
        mejora = super().create(data)

        mejora.createProblems(problems)
        mejora.createActions(actions)
        mejora.save()
        return mejora

    def update(self, data):
        if "problems" in data:
            del data['problems']
        if "actions" in data:
            del data['actions']
        if "project" in data:
            del data['project']
        return super().update(data)

    def createProblems(self, data):
        from models.fltrainb.problem import problem as Problem
        problems = []
        for problem in data:
            problem['improvement'] = self
            p = Problem().create(problem)
            problems.append(p)
        return problems

    def createActions(self, data):
        from models.fltrainb.action import action as Action

        actions = []
        for action in data:
            action['improvement'] = self
            action['state'] = 'Pendiente'
            actions.append(Action().create(action))
        return actions

    def get_problems(self):
        return self.problems.all()

    def get_actions(self):
        return self.actions.all()

    class Meta:
        abstract = True


# @class_declaration improvement #
class improvement(trainb_improvement):
    pass

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Usuarios", u"MetaData")
        db_table = u"improvement"
