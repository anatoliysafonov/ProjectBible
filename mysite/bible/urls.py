from django.urls import path
from . import views

app_name = 'bible'

urlpatterns = [
    path('<str:book>/<int:chapter>', views.index, name='root'),
    path('primitku/', views.page404, name='page404'),
]
