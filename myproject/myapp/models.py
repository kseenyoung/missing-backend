from django.db import models

class MChild(models.Model):
    name=models.TextField()
    gender=models.TextField(null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    ageNow=models.IntegerField(null=True, blank=True)
    alldressing=models.TextField(null=True, blank=True)
    occrAdd=models.TextField(null=True, blank=True)
    occrDate=models.TextField(null=True, blank=True)
    writngTarget=models.TextField(null=True, blank=True)
    inform=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
