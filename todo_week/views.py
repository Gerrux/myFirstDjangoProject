from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
week = {
    "monday": "понедельник",
    "tuesday": "вторник",
    "wednesday": "среду",
    "thursday": "четверг",
    "friday": "пятницу",
    "saturday": "субботу",
    "sunday": "воскресение",
}


def index(request):
    days = list(week)
    context = {
        'days': days
    }
    return render(request, 'todo_week/index.html', context=context)


def greeting(request):
    return render(request, 'todo_week/greeting.html')


def get_info_about_todo_week(request, week_day: str):
    description = week.get(week_day, None)
    if description:
        return HttpResponse(f"<h2>Список дел в {description}.</h2>")
    else:
        return HttpResponseNotFound(f"{week_day} - не найден.")


def get_info_about_todo_week_by_int(request, week_day: int):
    week_day -= 1
    if week_day in range(len(week)):
        name_zodiac = list(week)[week_day]
        redirect_url = reverse('todo-week-url', args=(name_zodiac, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"{week_day+1} - не найден.")
