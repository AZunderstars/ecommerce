from rest_framework import generics

from core.models import User
from users.serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
