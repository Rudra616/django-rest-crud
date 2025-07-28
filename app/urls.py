from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('StudentAll', StudentAll, basename='StudentAll')  # ModelViewSet

router1 = DefaultRouter()
router1.register('students1', StudentViewSet, basename='student')  # ViewSet


urlpatterns = [
    #FUNTION BASED
    path('students/',studentsView,name='studentsView'),
    path('students/<int:pk>/',studentdetailsView),

    #CLASS BASED
    path('class/students/',StudentListCreateView.as_view()),
    path('class/student/<int:pk>',StudentDetailsView.as_view()),

    # Generic Class-Based Views
    path('class/generic/students/',StudentListCreateViewGenrics.as_view()),
    path('class/generic/student/<int:pk>',StudentDetailsViewGenrics.as_view()),
    # check pagijnaiton http://127.0.0.1:8000/class/generic/students/?page-num=1
    # Viewset
    path('h1/', include(router.urls)),  # <--- THIS is required
    path('h2/', include(router1.urls)),



]