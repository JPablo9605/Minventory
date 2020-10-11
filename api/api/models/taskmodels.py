from django.db import models


# Create your models here.
class Task(models.Model):
    # Al momento de crearse una tarea, quiere decir que fue aprobada
    # por ende, la fecha de aprobacion es el dia en que se crea
    # y en consecuencia, se crea automaticamente
    approved_date = models.DateField(auto_now_add=True)

    # La @realization_date tiene que ser asignada por el admin, es la
    # fecha en que se realiza el trabajo, por tanto no es autoasignada
    # Formato: YYYY-MM-DD
    realization_date = models.DateField()
    fkAssignment_worker = models.IntegerField(default=0)
    fkElement_id = models.IntegerField(default=0)
    fkTask_status = models.IntegerField(default=0)
