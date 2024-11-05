from django.db import models

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.IntegerField()
    eadd=models.CharField(max_length=100)

    def __str__(self):
        return str(self.eno) + "\t" + self.ename + "\t" + str(self.esal) + "\t" + self.eadd;
