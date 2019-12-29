from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<str:name>', views.results, name='results'),
    path('person/<int:id>', views.person, name='person')
]