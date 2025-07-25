from rest_framework import serializers
from app.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta: # extra information for serilalizer like model or fields
        model = student 
        fields = "__all__"



