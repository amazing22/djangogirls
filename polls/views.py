from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, JHJ2(엄혜진, 양지선, 이지수)world. You're at the polls index.")
