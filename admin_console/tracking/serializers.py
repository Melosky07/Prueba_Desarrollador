from rest_framework import serializers
from .models import Session, ButtonClick
from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'is_admin']

class SessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    session_duration = serializers.ReadOnlyField()  
    button1_clicks = serializers.IntegerField(source='buttonclick_set.count', read_only=True)  
    button2_clicks = serializers.IntegerField(source='buttonclick_set.count', read_only=True)  
    class Meta:
        model = Session
        fields = ['id', 'user', 'start_time', 'end_time', 'session_duration', 'button1_clicks', 'button2_clicks']

class ButtonClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonClick
        fields = ['id', 'session', 'button_number', 'click_time']