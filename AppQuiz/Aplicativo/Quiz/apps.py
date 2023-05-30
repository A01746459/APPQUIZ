"""
 Final Project: Quiz Application with Microservices
 Date: 30-Nov-2022
 Authors:
        Jeovani Hernandez Bastida A01749164
        José Miguel Garcia Gurtubay Moreno A01373750
        Sebastian Burgos Alanís A01746459
        Sandra Ximena Téllez Olvera A01752142  
"""

### App Configuration with a Data Base ###

from django.apps import AppConfig

class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Quiz'
