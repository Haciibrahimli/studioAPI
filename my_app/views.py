from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView,DestroyAPIView)


from my_app.models import *
from my_app.serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()


class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    lookup_field = 'id'

class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'

class OurServicesListAPIView(ListAPIView):
    queryset = OurServices.objects.all()
    serializer_class = OurServicesSerializer
    permission_classes = [AllowAny]

class OurServicesRetrieveAPIView(RetrieveAPIView):
    queryset = OurServices.objects.all()
    serializer_class = OurServicesSerializer
    lookup_field = 'id'
   

class PartniorsListAPIView(ListAPIView):
    queryset = Partniors.objects.all()
    serializer_class = PartniorsSerializer
    lookup_field = 'id'

class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class BlogCategoryListAPIView(ListAPIView): 
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [AllowAny]
   

class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
    
class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
    # --


class BlogRetrieveAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'


class SosialMediaUpdateAPIView(UpdateAPIView):
    queryset = SosialMedia.objects.all()
    serializer_class = SosialMediaSerializer
    lookup_field = 'id'



class MainDetailsListAPIView(ListAPIView):
    queryset = MainDetails.objects.all()
    serializer_class = MainDetailsSerializer



class ProjectsListAPIView(ListAPIView): #CreateApi ce ListApi de  "id" lazim deyil
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [AllowAny]
   
class ProjectsRetrieveAPIView(RetrieveAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'id'
    
