from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^usuarios/$', views.UsuarioList.as_view(), name='usuario-list'),

]