from rest_framework import serializers
from employeeApp.models import Departments, Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId',
                'DepartmentName')

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId',
                'EmployeeName',
                'Department',
                'DateOfJoining',
                'PhotoName')
