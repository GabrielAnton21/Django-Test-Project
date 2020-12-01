from django.conf.urls import include
from django.urls import path
from. import views

urlpatterns = [
    path('', views.tasks, name="tasks"),
    path('update/<int:id>', views.update_task, name="update"),
    path('delete/<int:id>', views.delete_task, name="delete"),
    path('complete/<int:id>', views.complete_task, name="complete")
]