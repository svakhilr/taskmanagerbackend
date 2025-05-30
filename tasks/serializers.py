from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ('title','discription','due_date','priority','status')

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data["user"] = user
        return super().create(validated_data)

