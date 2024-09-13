from django.contrib import admin
from courses.models import Course, Module, Lesson, HomeWork


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(HomeWork)
class LessonAdmin(admin.ModelAdmin):
    pass
