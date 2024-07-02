from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.permissions import IsOwner
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsManager, IsNotManager


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsNotManager]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        elif self.action in ['update', 'retrieve', 'partial_update']:
            self.permission_classes = [IsManager | IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsNotManager]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsNotManager, IsOwner]
