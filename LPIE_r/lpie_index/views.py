from django.shortcuts import render
from courses.models import Course


# Create your views here.
def index(request):
    return render(request, 'index.html')


def courses(request):
    courses_db = Course.objects.all()
    context = {
        'courses': courses_db,
    }
    return render(request, 'courses.html', context)


def presentation(request):
    return render(request, 'LPIE-presentation.html')


def word(request):
    return render(request, 'LPIE-word.html')
