from django.db import models

class Exercise(models.Model):

    CARDIO = 'cardio'
    STRENGTH = 'strength'
    FLEXIBILITY = 'flexibility'

    TYPES_OF_EXERCISE = ((CARDIO, 'CARDIO'), (STRENGTH, 'STRENGTH'), (FLEXIBILITY, 'FLEXIBILITY'))

    name = models.CharField(max_length=256)
    type_of_exercise = models.CharField(max_length=251, choices=TYPES_OF_EXERCISE) 

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'exercise'
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'


class Activities(models.Model):

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, )
    activity_date = models.DateField()
    distance = models.FloatField(default=None, blank=True, null=True)
    time_taken = models.DurationField(default=None, blank=True, null=True)
    repetitions = models.IntegerField(default=None, blank=True, null=True)
    set_number = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        db_table = 'activity'
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
