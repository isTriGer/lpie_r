from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='courses_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'course'
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    number = models.IntegerField(verbose_name='Номер модуля в курсе')
    slug = models.SlugField(max_length=200, verbose_name='URL')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        db_table = 'module'
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    number = models.IntegerField(verbose_name='Номер урока в модуле')
    slug = models.SlugField(max_length=200, verbose_name='URL')
    module = models.ForeignKey(to=Module, on_delete=models.CASCADE, verbose_name='Модуль')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='Курс')
    theory = models.TextField(default='Странно ничего нет. Видимо для этого урока не предназначена теория', blank=True, null=True, verbose_name='Теория')

    class Meta:
        db_table = 'lesson'
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.name


class HomeWork(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    number = models.IntegerField(verbose_name='Номер задания в уроке')
    correct_answer = models.CharField(max_length=200, verbose_name='Ответ')
    hint = models.TextField(null=True, blank=True, verbose_name='Подсказка')
    module = models.ForeignKey(to=Module, on_delete=models.CASCADE, verbose_name='Модуль')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='Курс')
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, verbose_name='Урок')

    class Meta:
        db_table = 'home work'
        verbose_name = 'практика'
        verbose_name_plural = 'практики'
        ordering = ('id',)

    def __str__(self):
        return self.question

