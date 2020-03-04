from django.http import HttpResponse


def ical_test(request):
    f = open("./static/my.ics", mode='r')
    i = f.read()
    return HttpResponse(i)
