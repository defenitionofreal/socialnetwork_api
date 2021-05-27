from django.urls import path
from .views import registration, UserViewSet, UserAnalyticsApiView
from rest_framework.routers import DefaultRouter

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', registration, name='register'),
    path('users/analytics/', UserAnalyticsApiView.as_view())
]
urlpatterns += router.urls