from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=100)
    def __str__(self):
        return str(self.DepartmentName)
    class Meta:
        verbose_name_plural='Departments'
   


class Employees(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    DateOfJoining=models.DateField()
    PhotoName=models.CharField(max_length=100,)
    def __str__(self):
        return str(self.EmployeeId)+ " : " +self.EmployeeName
    class Meta:
        verbose_name_plural='Employees'
