from django.urls import path
from . import views
from django.contrib import admin
from django.contrib import staticfiles
from django.conf import settings # to import static in deployment
from django.conf.urls.static import static # to import static in deployment

admin.site.site_header = 'Developer Venkat'
admin.site.site_title = 'welcome to venki\'s Dashboard'
admin.site.index_title = 'Welcome to this Portal'

urlpatterns = [
    path('', views.welcome,name='home'),
    path('about/', views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('competitiveprogramming/',views.cp,name='competitiveprogramming'),
    path('contact/',views.contact,name='contact'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns
