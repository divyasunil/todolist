from . import views
from django.urls import path, include

app_name = 'todoapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    # path('details', views.details, name='details'),
    # path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),

]
