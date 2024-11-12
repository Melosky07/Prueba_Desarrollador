from django.shortcuts import render
from rest_framework import viewsets
from .models import Session, ButtonClick
from .serializers import SessionSerializer, ButtonClickSerializer
from users.models import CustomUser
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ButtonClickViewSet(viewsets.ModelViewSet):
    queryset = ButtonClick.objects.all()
    serializer_class = ButtonClickSerializer

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)

    if user is not None:
        is_admin = user.is_staff  
        return JsonResponse({"message": "Login successful", "is_admin": is_admin}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
