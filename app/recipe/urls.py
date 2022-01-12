from django.urls.conf import include, path
from recipe.views import TagViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tags', TagViewSet )

app_name = 'recipe'


urlpatterns = [
    path('', include(router.urls)),
]
