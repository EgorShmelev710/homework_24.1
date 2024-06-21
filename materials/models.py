from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='courses', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lessons', verbose_name='картинка', **NULLABLE)
    url = models.URLField(verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
