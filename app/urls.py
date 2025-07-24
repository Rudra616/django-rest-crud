from django.urls import path
from .views import *

urlpatterns = [
    path('students/',studentsView,name='studentsView'),
    path('students/<int:pk>/',studentdetailsView),
    # path('employee/',Employees.as_view()),
    # path('employee/<int:pk>',EmployeesDetail.as_view())
]