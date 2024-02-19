from django.urls import path
from my_app.views import *

urlpatterns = [
    path("about/list/<id>",AboutListAPIView.as_view(), name='about-list'),
    path("team/list/<id>", TeamListAPIView.as_view(), name='team-list'),
    path("ourservices/<id>", OurServicesListAPIView.as_view(), name='ourservices-list'),
    path("partnior/list/<id>",PartniorsListAPIView.as_view(), name='partnior-list'),
    path("contact/list",ContactListView.as_view(), name='contact-list'),
    path("blogcategory/list/",BlogCategoryListAPIView.as_view(), name='list-blogcategory'),
    path("blog/create",BlogCreateAPIView.as_view(), name='blog-create'),
    path("blog/retrieve/<id>/'",BlogRetrieveAPIView.as_view(), name='blog-retrieve'),
    path("blog/delate/<id>",BlogDestroyAPIView.as_view(), name='blog-delate'),
    path("sosial/media/<id>",SosialMediaUpdateAPIView.as_view(), name='sosial-media'),
    path("main/detail/destroy/<id>",MainDetailsRetrieveAPIView.as_view(), name='main-detail-destroy'),
]