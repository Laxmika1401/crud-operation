from django.db import models

# Create your models here.
class Employee(models.Model):
    EMPLOYEE_ID = models.CharField(max_length=255, primary_key=True)
    EMAIL_ID = models.EmailField(max_length=100)
    AGE = models.CharField(max_length=100)
    OCCUPATION = models.CharField(max_length=100)


    def __str__(self):
        return self.EMPLOYEE_ID
    

   
