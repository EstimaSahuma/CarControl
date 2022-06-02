from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^veiculo/listar/(?P<categoria>[\w\-]+)/$', views.listar_veiculo, name='listar_veiculo'),
    re_path(r'^veiculo/perfil/(?P<pk>[0-9]+)', views.perfil_veiculo, name='perfil_veiculo'),
]