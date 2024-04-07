from rest_framework import serializers
from django.utils import timezone
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    due_date = serializers.DateField()

    class Meta:
        model = Task
        fields =[ 'id', 'title', 'description', 'completed', 'due_date']

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value