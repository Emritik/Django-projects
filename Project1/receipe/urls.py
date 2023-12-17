from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import  settings
from receipe import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name='home'),
    path("delete/<id>/", views.delete, name='Delete_Receipe'),
    path("update/<id>/", views.update, name='Update_Receipe'),
    #This 3 lines of code only used for  authentication perpose. 
    #path("login", views.login_user, name='Login_Receipe'),
    #path("register", views.register, name='Register_Receipe'),  
   #path("logout",views.logout_user, name='Logout_Receipe')
    ]
#This part of code use when we want to take a image as input from the userend in oulic or media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()