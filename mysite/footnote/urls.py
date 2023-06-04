from django.urls import path
from . import views

app_name = 'footnote'

urlpatterns = [
    path('<str:code>', views.root, name='root'),
]