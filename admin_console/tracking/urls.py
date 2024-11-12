from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SessionViewSet, ButtonClickViewSet, login_view

router = DefaultRouter()
router.register(r'sessions', SessionViewSet)
router.register(r'button-clicks', ButtonClickViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]
