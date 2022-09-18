from django.contrib import admin
from django.urls import path, include
from home import views

# admin header customization

admin.site.site_header = "Developer Adarsh"
admin.site.site_title = "Welcome Adarsh"
admin.site.index_title = "Welcome to the admin portal"
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('contact', views.contact, name="contact")

]
