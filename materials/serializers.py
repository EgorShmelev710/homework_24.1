from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    @staticmethod
    def get_lessons_count(instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'
