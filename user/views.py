from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
import pdb
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.exceptions import ValidationError


# Create your views here.

class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.

    def post(self, request):
        req_user = request.data
        user = User(email=req_user.get('email'), first_name=req_user.get('first_name'),
                last_name=req_user.get('last_name'))
        user.set_password(req_user.get('password'))
        user.save()
        return Response({'message': 'successfully created'}, status=201)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'login successfully', 'user':serializer.data}, status=200)

class UserRetrieveUpdateDestroyAPIView(APIView):
    
    permission_classes = (IsAuthenticated,)
    # serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """ Get specific user from the system. """

        try:
            logged_in_user = request.user
            user = User()
            user_obj = User.objects.filter(id=logged_in_user.id).first()
            if user_obj is None:
                result = Response(
                    {'message': 'not exits'}, status=400)
            else:
                data = {
                    "first_name": user_obj.first_name,
                    "last_name": user_obj.last_name,
                    "email": user_obj.email,
                }
                result = Response(data, status=200)
        except ValidationError as e:
            result = Response({"message": e}, status=400)

        return result