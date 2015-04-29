from datetime import datetime
from django.shortcuts import render
import numberrr


def hello_world(request):
    a = numberrr.mulmul(808080800)
    return render(request, 'hello_world.html', {'current_time': datetime.now(), 'number': a})
