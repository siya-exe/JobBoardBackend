from rest_framework import serializers
from .models import Application
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


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.ReadOnlyField(source='applicant.username')
    job_title = serializers.ReadOnlyField(source='job.title')

    class Meta:
        model = Application
        fields = ['id', 'job', 'job_title', 'applicant', 'cover_letter', 'status', 'applied_on']
        read_only_fields = ['applicant', 'status', 'applied_on']
