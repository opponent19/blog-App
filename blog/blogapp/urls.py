

from django.urls import path
from blogapp import views

urlpatterns = [
    
    
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    #path('home/<x>/<y>',views.homepage),
    path('hello',views.hellowview),
    path('',views.homepage),
    path('userdashboard',views.user_dashboard),
    path('createblog',views.create_blog),
    path('see-det/<rid>',views.view_details),
    path('publish/<status>/<rid>',views.is_published),
    path('setcookie',views.setcookies),
    path('getcookie',views.getcookies),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('dform',views.djangoForm),
    
]
