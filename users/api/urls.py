from django.urls import path

from users.api.views import CreateUserApiView


urlpatterns = [
    path('create_user/', CreateUserApiView.as_view()),
]
