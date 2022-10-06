from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from .serializers import MyTokenObtainPairSerializer
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

# Custom permissions
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return hasattr(request.user, 'role')
        else:
            return hasattr(request.user, 'role') and request.user.role == 'ADMIN'

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer