from django.shortcuts import render
from .models import *
from .serilaizers import *
from rest_framework.response import Response
# send data back from your API view to the client (like frontend or Postman).
from rest_framework import status
# This gives you HTTP status codes (like 200, 201, 400, 404) as constants with names, so your code is easy to read.
from rest_framework.decorators import api_view
# It is a decorator that tells Django:
# 👉 "This view is a REST API function, not a regular Django view"
# from employee.models import Employee
# from rest_framework.views import APIView
# from django.http import Http404
# Create your views here.

@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students = student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data) #  ✅ Getting POST data
        if serializer.is_valid():  # ✅ Validating
            serializer.save()      # ✅ Saving to DB      
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(["GET","PUT","DELETE"])
def studentdetailsView(request,pk):
    try:
        students = student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerializer(students)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = StudentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeesDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)