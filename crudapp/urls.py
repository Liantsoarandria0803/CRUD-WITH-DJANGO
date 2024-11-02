from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('addTask',views.addTasks,name="addTasks"),
    path('updateTask/<str:pk>',views.updateTask,name="updateTask"),
    path('deleteTask/<str:pk>',views.deleteTask,name="deleteTask"),
    path('updateTaskForm/<str:pk>',views.updateTaskForm,name="updateTaskForm")
]
