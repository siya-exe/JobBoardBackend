from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CategoryViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = router.urls




