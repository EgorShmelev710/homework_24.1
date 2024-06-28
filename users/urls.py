from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentsListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments'),
] + router.urls
