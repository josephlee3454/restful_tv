from django.db import models

# Create your models here.
class ShowManager(models.Manager):
       # No fields should be a blank 
        # title at east two characters
        # network " 3 chars
        # desc 10
    def validateShow(self, postData):
        errors = {}

        if len(postData["release"]) <=10:
            errors["release"] = "Release date must not be blank"
        if len(postData["title"]) <2:
            errors["title"] = "Title msut be more than 2 char"
        if len(postData["network"]) <3:
            errors["network"] = "Title msut be more than 2 char"
        if len(postData["desc"]) <10:
            errors["desc"] = "Title msut be more than 2 char"
        return errors

     





class NewShow(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    release = models.DateField()
    desc = models.TextField()

    objects = ShowManager()

    def __str__(self):
       return self.title + " " + self.network + " "  + self.desc + f'{self.id}'
   