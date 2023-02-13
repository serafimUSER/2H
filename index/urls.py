from django.urls import path
from index.views import *


urlpatterns = [
    path('', index, name='index'),
    path('test/', test, name='test'),
    path('learning/', learning, name='learning'),
    path('about/', about, name='about')
]
