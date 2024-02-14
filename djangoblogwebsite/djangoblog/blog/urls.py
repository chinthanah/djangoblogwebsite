from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name='home'),
    path("blog/",views.blog,name='blog'),
    path("blogpost/<str:slug>",views.blogpost,name='blogpost'),
    path("contact/",views.contact,name='contact'),
    path("Search/",views.Search,name='Search')

]
