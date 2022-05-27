from django.urls import path
from .views import TaskList


app_name = 'pages'

urlpatterns = [
    path('', TaskList.as_view(), name='home'),
]
