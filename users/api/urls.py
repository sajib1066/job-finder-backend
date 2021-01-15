from django.urls import path

from users.api.views import CreateUserApiView, LoginView


urlpatterns = [
    path('create_user/', CreateUserApiView.as_view()),
    path('login/', LoginView.as_view()),
]
