from django.urls import path
from . import views

urlpatterns = [
    path("rectangle", views.rectangle_index),
    path("square", views.square_index),
    path("circle", views.circle_index),
    path("rectangle/<int:width>/<int:height>", views.get_rectangle_area, name='get-rectangle-area'),
    path("rectangle/<int:width>/<int:height>/", views.get_rectangle_area, name='get-rectangle-area'),
    path("square/<int:width>", views.get_square_area, name='get-square-area'),
    path("square/<int:width>/", views.get_square_area, name='get-square-area'),
    path("circle/<int:radius>", views.get_circle_area, name='get-circle-area'),
    path("circle/<int:radius>/", views.get_circle_area, name='get-circle-area'),
    path("get_rectangle_area/<int:width>/<int:height>", views.get_rectangle_area_by_src),
    path("get_square_area/<int:width>", views.get_square_area_by_src),
    path("get_circle_area/<int:radius>", views.get_circle_area_by_src),
    path("get_rectangle_area/<int:width>/<int:height>/", views.get_rectangle_area_by_src),
    path("get_square_area/<int:width>/", views.get_square_area_by_src),
    path("get_circle_area/<int:radius>/", views.get_circle_area_by_src),
]