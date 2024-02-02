from . import views
from django.urls import path, include

app_name = 'todoapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    # path('details', views.details, name='details'),
    # path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    # Generic View Links
    path('vhome/', views.Tasklistview.as_view(), name='vhome'),
    path('vdetail/<int:pk>/', views.TaskDetailView.as_view(), name='vdetail'),
    path('vupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='vupdate'),
    path('vdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='vdelete'),

]
