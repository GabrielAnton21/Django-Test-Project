from django.urls import path
from. import views

urlpatterns = [

    path('index', views.index, name="index"),
    path('update', views.update_task, name="update"),
    path('delete', views.delete_task, name="delete"),
    path('add', views.add_task, name="add"),
    path('complete', views.complete_task, name="complete")
]