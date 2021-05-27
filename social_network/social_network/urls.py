from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="Notes API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/v1/rest-auth/', include('rest_auth.urls')),
    # path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('users.urls'), name='jwtauth'),
    path('api/v1/docs/', schema_view),
]

