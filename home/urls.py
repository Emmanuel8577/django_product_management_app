from django.contrib import admin
from django.urls import path,include
from home import views

#Django admin customerzation

admin.site.site_header = "Welcome Emmanuel Adikwu"
admin.site.site_title = "Welcome Emmanuel to your Dashboard"
admin.site.index_title = "Welcome to your Portal"
urlpatterns = [
   path('', views.home, name='home'),
   path('about', views.about, name='about'),
   path('projects', views.projects, name='projects'),
   path('contact', views.Contact, name='contact')
  
]

