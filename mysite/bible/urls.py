from django.urls import path
from . import views

app_name = 'bible'

urlpatterns = [
    path('<str:book>/<int:chapter>', views.index, name='root'),
    path('', views.index, name='root_from_users'),
    path('ajax', views.ajax, name='ajax'),
]
