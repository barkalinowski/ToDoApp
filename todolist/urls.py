from django.urls import path
from .views import *

urlpatterns = [
    path('', tasksView, name = "list_view"),
    path('delete_task/<str:pk>', deleteView, name = "delete_view"),
    path('update_task/<str:pk>', updateView, name = "update_view")
]