from rest_framework import serializers
from .models import Project,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','picture_Main_pic', 'description', 'link','profile')