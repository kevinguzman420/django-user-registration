from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from .permissions import UserPermission
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-date_joined")
    permission_classes = [UserPermission]
