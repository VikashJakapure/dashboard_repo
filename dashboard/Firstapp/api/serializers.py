from rest_framework.serializers import ModelSerializer 
from Firstapp.models import *
class ITJobsSerializer(ModelSerializer):
    class Meta:
        model=ITJobs 
        fields='__all__'
