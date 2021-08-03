from django.urls import path

from . import views

app_name = 'assignments'
urlpatterns = [
    path('create_assignment/', views.create_assignment, name='create_assignment')
]
