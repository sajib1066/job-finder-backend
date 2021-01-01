from rest_framework.generics import CreateAPIView

from users.models import User
from users.api.serializers import CreateUserSerializer


class CreateUserApiView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
