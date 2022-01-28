from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {width*height}.")


def get_square_area(request, width: int):
    return HttpResponse(f"Площадь квадрата размером {width}х{width} равна {width**2}.")


def get_circle_area(request, radius: int):
    pi = 3.14
    return HttpResponse(f"Площадь окружности радиусом {radius} равна {pi*radius**2}.")


def get_rectangle_area_by_src(request, width: int, height: int):
    redirect_url = reverse('get-rectangle-area', args=(width, height,))
    return HttpResponseRedirect(redirect_url)


def get_square_area_by_src(request, width: int):
    redirect_url = reverse('get-square-area', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle_area_by_src(request, radius: int):
    redirect_url = reverse('get-square-area', args=(radius,))
    return HttpResponseRedirect(redirect_url)
