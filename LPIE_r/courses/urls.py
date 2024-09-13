from django.urls import path
from .views import current_course, lesson, practice


urlpatterns = [
    path('<slug:course_slug>/', current_course, name='current_course'),
    path('<slug:course_slug>/<slug:module_slug>/<slug:lesson_slug>/theory/', lesson, name='lesson'),
    path('<slug:course_slug>/<slug:module_slug>/<slug:lesson_slug>/practice/', practice, name='practice'),
    path('<slug:course_slug>/<slug:module_slug>/<slug:lesson_slug>/practice/<int:page>/', practice, name='practice'),
]
