from .views import RegistrationAPIView, LoginAPIView, CreateStoryAPIView
from django.urls import path

urlpatterns = [
    path('user/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('add_story/', CreateStoryAPIView.as_view())
]
