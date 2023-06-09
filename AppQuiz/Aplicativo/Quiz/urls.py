"""
 Final Project: Quiz Application with Microservices
 Date: 30-Nov-2022
 Authors:
        Jeovani Hernandez Bastida A01749164
        José Miguel Garcia Gurtubay Moreno A01373750
        Sebastian Burgos Alanís A01746459
        Sandra Ximena Téllez Olvera A01752142  
"""

### URLs Configuration ###

from django.urls import path
from .views import (
    inicio,
    registro, 
    loginView, 
    logout_vista, 
    HomeUsuario, 
    jugar,
    resultado_pregunta,
    tablero,
    seleccionarPreguntas)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),
    path('login/', loginView, name='login'),
    path('logout_vista/', logout_vista, name='logout_vista'),
    path('registro/', registro, name='registro'),
    path('tablero/', tablero, name='tablero'),
    path('seleccionarPreguntas/', seleccionarPreguntas, name='seleccionar_preguntas'),
    path('jugar/<int:cantidad_preguntas>/', jugar, name='jugar'),
    path('resultado/<int:pregunta_respondida_pk>', resultado_pregunta, name='resultado')
    
]
