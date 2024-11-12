from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SessionViewSet,
    ButtonClickViewSet,
    login_view,
    list_sessions,
    get_user_sessions
)

router = DefaultRouter()
router.register(r'sessions', SessionViewSet)
router.register(r'button-clicks', ButtonClickViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('login/', login_view, name='login'),
    path('sessions/', list_sessions, name='list_sessions'),
    path('user-sessions/', get_user_sessions, name='get_user_sessions'),
]
