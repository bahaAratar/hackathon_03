from rest_framework import status
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer  
from applications.account.serializers import RegisterSerializer, LoginSerializer
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MyUser, ResetPassword
from .serializers import MyUserSerializer

User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('вы успешно зарегистрировались. вам отправлено писбмо для подтверждения', status=201)

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Успешно'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Link expired'}, status=400)
        
# class ResetPasswordView(APIView):
#     def post(self, request, key):
#         try:
#             passw = ResetPassword.objects.get(key=key)
#             passw.key = ''
#             passw.save()
#             return Response({'msg': 'ok'}, status=200)
#         except ResetPassword.DoesNotExist:
#             return Response({'msg': 'error'}, status=400)

class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:    
            user = request.user
            token = Token.objects.get(user=user).delete()
            return Response('вы успешно разлогинились', status=200)
        except:
            return Response(status=403)
    
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyUserdViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]