from rest_framework import serializers
from app.models import *
# from employee.models import Employee

class StudentSerializer(serializers.ModelSerializer):
    class Meta: # extra information for serilalizer like model or fields
        model = student 
        fields = "__all__"



# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'