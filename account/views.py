from django.contrib.auth import login
from rest_framework import views, status, response, permissions

from .models import User
from .serializers import UserSignupSerializer, UserLoginSerializer


class SignupView(views.APIView):
    serializer_class = UserSignupSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request):
        phone = request.data.get('phone')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(phone=phone)
            login(request, user)
            return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
