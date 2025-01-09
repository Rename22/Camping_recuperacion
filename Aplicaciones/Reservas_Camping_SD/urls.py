from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion),
    path('cerrar_sesion/', views.cerrar_sesion),
    path('inicio/', views.pagina_inicio),
    path('registro/', views.registro_usuario),
]
