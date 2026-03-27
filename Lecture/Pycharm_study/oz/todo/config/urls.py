from django.contrib import admin
from django.urls import path, include
from todo import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_info, name='todo_info'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/<int:pk>/update/', views.todo_update, name='todo_update'),
    path('todo/<int:pk>/delete', views.todo_delete, name='todo_delete'),

    # account
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', user_views.signup, name='signup')
]
