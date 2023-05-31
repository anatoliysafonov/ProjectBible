from django.urls import path, include
from . import views

app_name = 'bible'

urlpatterns = [
    path('<int:chapter>', views.root, name='root'),
]
