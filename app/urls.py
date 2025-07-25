from django.urls import path
from .views import *

urlpatterns = [
    #FUNTION BASED
    path('students/',studentsView,name='studentsView'),
    path('students/<int:pk>/',studentdetailsView),

    #CLASS BASED
    path('class/students/',StudentListCreateView.as_view()),
    path('class/student/<int:pk>',StudentDetailsView.as_view())
]