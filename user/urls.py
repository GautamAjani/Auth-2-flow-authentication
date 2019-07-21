from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateDestroyAPIView
from django.urls import path

urlpatterns = [
    path('user/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('get_user/', UserRetrieveUpdateDestroyAPIView.as_view()),
]
