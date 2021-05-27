from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'posts'

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('posts/analytics/date_from=<date_from>&date_to=<date_to>/', PostLikesAnalyticsApiView.as_view(), name='posts-analytics')
]
urlpatterns += router.urls