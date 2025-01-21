from django.urls import path
from demoapp import views
urlpatterns = [
    path('', views.index, name='hello_world'),
    path('about/', views.about, name='about'),
]
