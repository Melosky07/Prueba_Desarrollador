from rest_framework import serializers
from .models import Session, ButtonClick
from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'is_admin']

class SessionSerializer(serializers.ModelSerializer):
    session_duration = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = ['id', 'user', 'start_time', 'end_time', 'session_duration']

class ButtonClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonClick
        fields = ['session', 'button_number', 'click_time']
