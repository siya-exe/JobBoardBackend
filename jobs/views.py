from rest_framework import viewsets, permissions
from .permissions import IsAdminUserRole
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Job, Category
from .serializers import JobSerializer, CategorySerializer

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
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUserRole]

    def get_permissions(self):
        """
        Apply IsAdminUserRole only to unsafe methods (POST, PUT, PATCH, DELETE)
        """
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUserRole()]
        return []  # Allow anyone to GET

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
