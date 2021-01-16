from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Profile
from users.api.serializers import CreateUserSerializer


class CreateUserApiView(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.create_user(email=email, password=password)
            profile = Profile.objects.create(user=user)
            if user and profile:
                return Response({
                    'message': 'Profile created successfully',
                    'user': user.email,
                    'status': status.HTTP_200_OK
                })
        else:
            return Response({
                'message': 'Invalid Request',
                'error': serializer.errors,
                'status': status.HTTP_403_FORBIDDEN
            })
