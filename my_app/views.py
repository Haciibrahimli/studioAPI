from django.shortcuts import render,redirect
from rest_framework.permissions import AllowAny
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView,DestroyAPIView)

from my_app.filters import BlogFilter
from django_filters.rest_framework.backends import DjangoFilterBackend


from my_app.models import *
from my_app.serializers import *
from django.contrib.auth import get_user_model
# -->Translate imports
from django.urls import reverse, translate_url
from django.conf import settings



User = get_user_model()

def set_language(request, lang_code): # translate
    referer = request.META.get("HTTP_REFERER")

    if referer:
        response = redirect(translate_url(referer, lang_code))
    else:
        response = redirect(reverse('home'))

    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response


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


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BlogFilter


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



class ProjectsListAPIView(ListAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [AllowAny]
   
class ProjectsRetrieveAPIView(RetrieveAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'id'
    
