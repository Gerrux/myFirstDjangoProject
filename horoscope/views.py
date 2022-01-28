from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date

# Create your views here.
zodiac_dict = {
    "aries": {
        "description": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
        "element": "fire",
        "start_date": date(2022, 3, 21),
        "end_date": date(2022, 4, 20),
    },
    "taurus": {
        "description": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
        "element": "earth",
        "start_date": date(2022, 4, 21),
        "end_date": date(2022, 5, 21),
    },
    "gemini": {
        "description": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
        "element": "air",
        "start_date": date(2022, 5, 22),
        "end_date": date(2022, 6, 21),
    },
    "cancer": {
        "description": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
        "element": "water",
        "start_date": date(2022, 6, 22),
        "end_date": date(2022, 7, 22),
    },
    "leo": {
        "description": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
        "element": "fire",
        "start_date": date(2022, 7, 23),
        "end_date": date(2022, 8, 21),
    },
    "virgo": {
        "description": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
        "element": "earth",
        "start_date": date(2022, 8, 22),
        "end_date": date(2022, 9, 23),
    },
    "libra": {
        "description": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
        "element": "air",
        "start_date": date(2022, 9, 24),
        "end_date": date(2022, 10, 23),
    },
    "scorpio": {
        "description": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
        "element": "water",
        "start_date": date(2022, 10, 24),
        "end_date": date(2022, 11, 22),
    },
    "sagittarius": {
        "description": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
        "element": "fire",
        "start_date": date(2022, 11, 23),
        "end_date": date(2022, 12, 22),
    },
    "capricorn": {
        "description": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
        "element": "earth",
        "start_date": date(2022, 12, 23),
        "end_date": date(2023, 1, 20),
    },
    "aquarius": {
        "description": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
        "element": "air",
        "start_date": date(2022, 1, 21),
        "end_date": date(2022, 2, 19),
    },
    "pisces": {
        "description": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)",
        "element": "water",
        "start_date": date(2022, 2, 20),
        "end_date": date(2022, 3, 20),
    }
}


def index(request):
    li_elements = ""
    for sign in list(zodiac_dict):
        redirect_url = reverse('zodiac-name', args=(sign,))
        li_elements += f"<li><a href='{redirect_url}'>{sign.title()}</a></li>"
    response = f"""
    <ol>
    {li_elements}
    </ol>
    """
    return HttpResponse(response)


def elements_zodiac(request):
    li_elements = ""
    elements = []
    for sign in list(zodiac_dict):
        elements.append(zodiac_dict[sign]['element'])
    elements = set(elements)
    for element in elements:
        redirect_url = reverse('zodiac-element', args=(element,))
        li_elements += f"<li><a href='{redirect_url}'>{element.title()}</a></li>"
    response = f"""
        <ol>
        {li_elements}
        </ol>
        """
    return HttpResponse(response)


def get_list_signs_zodiac(request, element: str):
    li_elements = ""
    for sign in list(zodiac_dict):
        if zodiac_dict[sign]['element'] == element:
            redirect_url = reverse('zodiac-name', args=(sign,))
            li_elements += f"<li><a href='{redirect_url}'>{sign.title()}</a></li>"
    response = f"""
        <ol>
        {li_elements}
        </ol>
        """
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    sign = zodiac_dict.get(sign_zodiac, None)
    description = sign['description']
    if description:
        return HttpResponse(f"<h2>{description}</h2>")
    else:
        return HttpResponseNotFound(f"{sign_zodiac} - не найден.")


def get_info_about_sign_zodiac_by_int(request, sign_zodiac: int):
    sign_zodiac -= 1
    if sign_zodiac in range(len(zodiac_dict)):
        zodiac = list(zodiac_dict)[sign_zodiac]
        redirect_url = reverse('zodiac-name', args=(zodiac,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"{sign_zodiac+1} - не найден.")


def get_info_by_date(request, month: int, day: int):
    try:
        selected_date = date(2022, month, day)
    except ValueError:
        return HttpResponseNotFound(f"Данные введены неверно.")
    for sign in list(zodiac_dict):
        if zodiac_dict[sign]['start_date'] < selected_date < zodiac_dict[sign]['end_date']:
            redirect_url = reverse('zodiac-name', args=(sign,))
            return HttpResponseRedirect(redirect_url)
