from django.urls import path, include
from . import views

"""
This file defines all URL patterns for the CryptoTutor web application. URLs are mapped
between this class and the associated view function for Django to process.
"""

urlpatterns = [
    path('<str:sort_type>', views.index, name='index'),
    path('', views.index, name='index'),
    path('question/<int:id>', views.question, name='question'),
    path('delete-question/<int:id>', views.delete_question, name='delete-question'),
    path('question-form/', views.questionForm, name='question-form'),
    path('code-form/', views.codeForm, name='code-form'),
    path('code-selection/', views.codeSelection, name='code-selection'),
    path('diff-viewer/', views.diffViewer, name='diff-viewer'),
    path('results/', views.nicadResults, name='nicad-results'),
    path('register/', views.register, name='register'),
    path('change-password/', views.changePassword, name='change-password')
]