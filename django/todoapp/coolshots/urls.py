from django.urls import path

from . import views

urlpatterns = [
    path('cool/', views.index, name="index"),
    path('cool/add', views.add, name="add"),
    path('cool/delete/<int:coolshot_id>', views.delete, name="delete"),
    path('cool/update/<int:coolshot_id>', views.update, name="update"),
    path('', views.home, name="home"),
]
