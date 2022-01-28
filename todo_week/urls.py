from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:week_day>", views.get_info_about_todo_week_by_int),
    path("<int:week_day>/", views.get_info_about_todo_week_by_int),
    path("<str:week_day>", views.get_info_about_todo_week, name='todo-week-url'),
    path("<str:week_day>/", views.get_info_about_todo_week, name='todo-week-url'),
]