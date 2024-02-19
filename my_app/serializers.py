from rest_framework import serializers
from my_app.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Team
        fields = "__all__"

class OurServicesSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = OurServices
        fields = "__all__"

class PartniorsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Partniors
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Contact
        fields = "__all__"



class SosialMediaSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = SosialMedia
        fields = "__all__"


class MainDetailsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = MainDetails
        fields = "__all__"

class BlogCategorySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = BlogCategory
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Blog
        fields = "__all__"

class ProjectsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Projects
        fields = "__all__"