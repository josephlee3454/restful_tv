from django.db import models

# Create your models here.
class NewShow(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    release = models.DateField()
    desc = models.TextField()

    def __str__(self):
       return self.title + " " + self.network + " "  + self.desc + f'{self.id}'
  