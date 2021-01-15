from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from users.api.serializers import LoginSerializer
from users.models import User


class LoginView(APIView):
    http_method_names = ['post']
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                get_user = User.objects.get(email=email)
                user_auth = authenticate(email=email, password=password)
                access_token = AccessToken.for_user(user_auth)
                refresh_token = RefreshToken.for_user(user_auth)
                if user_auth:
                    login(request, user_auth)
                    return Response({
                        'message': 'Login successful',
                        'email': get_user.email,
                        'last_login': get_user.last_login,
                        'is_candidate': get_user.is_candidate,
                        'is_employee': get_user.is_employee,
                        'is_active': get_user.is_active,
                        'access_token': str(access_token),
                        'refresh_token': str(refresh_token),
                        'status': status.HTTP_200_OK
                    })
                else:
                    return Response({
                        'message': 'User not found',
                        'status': status.HTTP_404_NOT_FOUND
                    })
            except User.DoesNotExist:
                return Response({
                    'message': 'User not found',
                    'status': status.HTTP_404_NOT_FOUND
                })
        else:
            return Response({
                'message': 'Invalid Request',
                'status': status.HTTP_403_FORBIDDEN
            })
