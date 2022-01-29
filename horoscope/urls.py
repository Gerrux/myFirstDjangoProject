from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello', views.hello_world),
    path('<int:month>/<int:day>/', views.get_info_by_date),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('type', views.elements_zodiac),
    path('type/', views.elements_zodiac),
    path('type/<str:element>/', views.get_list_signs_zodiac, name='zodiac-element'),
    path('type/<str:element>', views.get_list_signs_zodiac, name='zodiac-element'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_int),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_int),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='zodiac-name'),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='zodiac-name')
]