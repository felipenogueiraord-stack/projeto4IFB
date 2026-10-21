from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from filmes.views import FilmesViewSet, GenerosViewSet


router = DefaultRouter()

router.register('generos', GenerosViewSet, basename='generos')
router.register('filmes', FilmesViewSet, basename='filmes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token'),
]
