from django.urls import path
from cowsay import views

urlpatterns = [
    path('', views.create_cowsay, name='homepage'),
    path('history/', views.history)
]
