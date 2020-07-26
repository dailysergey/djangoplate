from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Daily_sergey'
    _context = {'date': date, 'name': name}
    return render(request, 'home.html', context=_context)
