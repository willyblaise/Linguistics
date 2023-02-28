from django.urls import path

from . import views

urlpatterns = [
    path('todolist/', views.indext, name="indext"),
    path('todolist/add', views.add, name="add"),
    path('todolist/delete/<int:todo_id>', views.delete, name="delete"),
    path('todolist/update/<int:todo_id>', views.update, name="update"),
    path('todolist/resume', views.resume, name="resume"),
]
