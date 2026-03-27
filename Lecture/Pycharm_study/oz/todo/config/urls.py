from django.contrib import admin
from django.urls import path, include
from todo import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_info, name='todo_info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', user_views.signup, name='signup')
]
