from django.urls import path
from .views import index, courses, presentation, word


urlpatterns = [
    path('', index, name='main'),
    path('courses/', courses, name='courses'),
    path('presentation/', presentation, name='presentation'),
    path('word/', word, name='word'),
]
