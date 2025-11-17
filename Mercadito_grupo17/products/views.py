from rest_framework import viewsets, permissions
from rest_framework.permissions import SAFE_METHODS
from .models import Product
from .serializers import ProductSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):  # Permite lectura a todos; escritura solo al owner.
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # si owner es None, no permitimos editar (a menos que seas superuser)
        user = getattr(request, "user", None)
        if user and user.is_superuser:
            return True
        return obj.owner == user

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    # Exigir autenticación para métodos no seguros, además chequear owner
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Asigna owner automáticamente (usuario autenticado)
        serializer.save(owner=self.request.user)