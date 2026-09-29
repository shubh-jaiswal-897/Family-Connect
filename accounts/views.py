from rest_framework import generics
from rest_framework.permissions import AllowAny
from accounts.models import User
from accounts.serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
