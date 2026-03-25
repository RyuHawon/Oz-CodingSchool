from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.todo_list),
    path('todo/<int:pk>/', views.todo_info)
]
