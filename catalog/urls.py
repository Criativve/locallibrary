from django.urls import path
import catalog.views as views

urlpatterns = [
    path('', views.index, name='index'),
]