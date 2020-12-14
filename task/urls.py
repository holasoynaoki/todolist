from django.contrib import admin
from django.urls import path
from .views import *
# from .views import index, todo_post, delete

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('todo_post/', todo_post, name='todo_post'),
    path('delete/<str:task_id>', delete, name='delete'),
    path('update/<str:task_id>', update, name='update'),
    path('edit/<str:task_id>', edit, name='edit'),
    # path('is_edit/<str:task_id>', is_edit, name='is_edit'),
    # path('vamos/<str:task_id>', vamos, name='vamos'),
]