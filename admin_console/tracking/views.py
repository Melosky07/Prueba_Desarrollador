from django.shortcuts import render
from rest_framework import viewsets
from .models import Session, ButtonClick
from .serializers import SessionSerializer, ButtonClickSerializer, SimplifiedSessionSerializer
from users.models import CustomUser
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ButtonClickViewSet(viewsets.ModelViewSet):
    queryset = ButtonClick.objects.all()
    serializer_class = ButtonClickSerializer

class SimplifiedSessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SimplifiedSessionSerializer

@api_view(['GET'])
def list_sessions(request):
    sessions = Session.objects.all()
    serializer = SessionSerializer(sessions, many=True)
    return Response(serializer.data)

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


@api_view(['GET'])
def get_user_sessions(request):
    users = CustomUser.objects.filter(is_staff=False)  
    data = []

    for user in users:
        user_sessions = Session.objects.filter(user=user)  
        user_data = {
            'username': user.username,
            'sessionDuration': sum(s.session_duration or 0 for s in user_sessions),  
            'button1Clicks': sum(s.button1_clicks for s in user_sessions),  
            'button2Clicks': sum(s.button2_clicks for s in user_sessions),  
        }
        data.append(user_data)

    return Response(data)

def perform_create(self, serializer):
    serializer.save(user=self.request.user)
