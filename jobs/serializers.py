from rest_framework import serializers
from .models import Job, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'category', 'category_id', 'location', 'job_type', 'posted_by', 'created_at']
        read_only_fields = ['posted_by', 'created_at']
