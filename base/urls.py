from django.urls import path
from . views import TaskList, TaskCreate, TaskUpdate, TaskDelete


urlpatterns = [  
    path('', TaskList.as_view(), name = 'tasks'),
    path('create-task/', TaskCreate.as_view(), name = 'create'),
    path('update-task/<slug:slug>/', TaskUpdate.as_view(), name = 'update'),
    path('delete-task/<slug:slug>/', TaskDelete.as_view(), name = 'delete'),
]
