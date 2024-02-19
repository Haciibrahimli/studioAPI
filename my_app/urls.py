from django.urls import path
from my_app.views import *

urlpatterns = [
    path("about/list",AboutListAPIView.as_view(), name='about-list'),
    path("team/list", TeamListAPIView.as_view(), name='team-list'),
    path("ourservices", OurServicesListAPIView.as_view(), name='ourservices-list'),
    path("ourservices/detail/<id>/", OurServicesRetrieveAPIView.as_view(), name='ourservices-detail'),
    path("partnior/list",PartniorsListAPIView.as_view(), name='partnior-list'),
    path("contact/list",ContactListView.as_view(), name='contact-list'),
    path("blogcategory/list/",BlogCategoryListAPIView.as_view(), name='list-blogcategory'),
    path("blog/create",BlogCreateAPIView.as_view(), name='blog-create'),
    path("blog/retrieve/<id>/'",BlogRetrieveAPIView.as_view(), name='blog-retrieve'),
    path("sosial/media",SosialMediaUpdateAPIView.as_view(), name='sosial-media'),
    path("main/detail",MainDetailsListAPIView.as_view(), name='main-detail'),
]