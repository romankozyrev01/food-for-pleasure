from rest_framework import routers
from .views import ActivityViewSet, MealViewSet, ActivityUserViewSet, MealUserViewSet


router = routers.SimpleRouter()
router.register('activities', ActivityViewSet)
router.register('meal', MealViewSet)
router.register('my_meal', MealUserViewSet)
router.register('my_activity', ActivityUserViewSet)


urlpatterns = router.urls
