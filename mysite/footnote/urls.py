from django.urls import path
from . import views

app_name = 'footnote'

urlpatterns = [
    path('', views.root, name='root'),
]