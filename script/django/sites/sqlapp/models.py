from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.name, self.passwd)

    class Admin:
        pass
