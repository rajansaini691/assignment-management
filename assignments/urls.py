from django.urls import path

from . import views

app_name = 'assignments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create_assignment_template, name='create'),
    path('<int:pk>/edit/', views.edit_assignment_template, name='edit'),
    path('<int:pk>/save/', views.save_assignment_template, name='save'),
    path('<int:pk>/generate/', views.generate_assignments, name='generate'),
]
