from django.urls.conf import include, path
from recipe.views import TagViewSet, IngredientViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)

app_name = 'recipe'


urlpatterns = [
    path('', include(router.urls)),
]
