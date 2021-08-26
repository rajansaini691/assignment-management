from django.urls import path

from . import views

app_name = 'assignments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create_assignment, name='create'),
    path('<int:pk>/edit/', views.edit_assignment, name='edit'),
    path('<int:pk>/save/', views.save_assignment, name='save'),
]
