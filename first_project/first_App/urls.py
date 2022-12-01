from django.urls import path
from first_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('educative/', views.educative, name='educative'),
    path('<age>/', views.show_age, name="show_age"),
    path('<int:num>/', views.even_or_odd, name="even_or_odd"),
    path('forms/', views.forms, name="form")
]