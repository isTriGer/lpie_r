from django.core.paginator import Paginator
from django.shortcuts import render
from courses.models import Course
from courses.models import Module
from courses.models import Lesson
from courses.models import HomeWork


# Create your views here.
def current_course(request, course_slug):
    course_info = Course.objects.get(slug=course_slug)
    modules = Module.objects.filter(course__slug=course_slug)
    lessons = Lesson.objects.filter(course__slug=course_slug)
    context = {
        'course': course_info,
        'modules': modules,
        'lessons': lessons,
    }
    return render(request, 'current_course.html', context=context)


def lesson(request, course_slug, module_slug, lesson_slug):
    lesson_info = Lesson.objects.get(slug=lesson_slug)
    context = {
        'lesson': lesson_info,
        'course_slug': course_slug,
        'module_slug': module_slug,
    }
    return render(request, 'lesson.html', context)


def practice(request, course_slug, module_slug, lesson_slug, page=1):
    home_work_info = HomeWork.objects.filter(lesson__slug=lesson_slug)
    paginator = Paginator(home_work_info, 1)
    current_page = paginator.page(page)
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        answer = request.POST.get('answer')
        homework = HomeWork.objects.get(id=question_id)
        if answer.lower() == homework.correct_answer.lower():
            result = "Correct!"
        else:
            result = f"Incorrect. The correct answer is: {homework.correct_answer}"
            if homework.hint:
                result += f"\nHint: {homework.hint}"
        return render(request, 'lesson_practice.html', {
                                                        'result': result,
                                                        'lesson_slug': lesson_slug,
                                                        'course_slug': course_slug,
                                                        'module_slug': module_slug,
                                                        'hw': current_page,
                                                        })

    else:
        context = {
            'hw': current_page,
            'lesson_slug': lesson_slug,
            'course_slug': course_slug,
            'module_slug': module_slug,
        }
        return render(request, 'lesson_practice.html', context)
