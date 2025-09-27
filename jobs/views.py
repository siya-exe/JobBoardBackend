from rest_framework import viewsets, permissions, filters
from .permissions import IsAdminUserRole
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Job, Category
from .serializers import JobSerializer, CategorySerializer
from .models import Application
from .serializers import ApplicationSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'admin'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location', 'category__name', 'job_type']
    ordering_fields = ['created_at', 'title']

    def get_permissions(self):
        """
        Apply IsAdminUserRole only to unsafe methods (POST, PUT, PATCH, DELETE)
        """
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUserRole()]
        return []  # Allow anyone to GET

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)



class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Application.objects.all()  # admin sees all applications
        return Application.objects.filter(applicant=user)  # users see their own

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
