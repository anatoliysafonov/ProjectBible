from django.urls import path, include
from . import views

app_name = 'bible'

urlpatterns = [
    path('<int:book>/<int:chapter>', views.root, name='root'),
    path('primitku/', views.page404, name='page404')
]
