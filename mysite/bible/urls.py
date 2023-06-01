from django.urls import path
from . import views

app_name = 'bible'

urlpatterns = [
    path('<int:book>/<int:chapter>', views.index, name='root'),
    path('primitku/', views.page404, name='page404'),
    path('<int:chapter>', views.root, name='root'),
]
