from django.urls import path, include
from .views import home,registro_usuario
from . import views

app_name='sesion'

urlpatterns=[
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro_usuario, name='registro'),
    path("password_reset", views.password_reset_request, name="password_reset")
 
]