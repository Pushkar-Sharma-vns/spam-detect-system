from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import views, response, status, generics, filters

from account.models import User
from .models import ContactList, SpamDatabase
from .serializers import ContactListSerializer, MarkSpamSerializer
from .pagination import CustomPagination


class ContactListView(LoginRequiredMixin, generics.ListAPIView):
    login_url = '/users/login/'
    search_fields = ['^name', 'name', 'contact_of__phone', 'phone']
    filter_backends = (filters.SearchFilter,)
    # queryset = ContactList.objects.all()
    pagination_class = CustomPagination
    serializer_class = ContactListSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = ContactList.objects.all()
        return queryset
    
    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context.update({"request": self.request})
    #     return context
    
class ContactView(LoginRequiredMixin, views.APIView):
    login_url = '/users/login/'
    
    def get(self, request, contact_id):
        contact_obj = ContactList.objects.get(id=contact_id)
        if contact_obj:
            serializer = ContactListSerializer(contact_obj)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'error': 'Contact does not exist.'}, status=400)
    
    '''
        User can give spam score from 1-10 to a particular contact.
    '''
    def patch(self, request, contact_id):
        contact_obj = ContactList.objects.get(id=contact_id)
        spam_score = request.data.get('spam_score')
        spam_score = 10 if spam_score > 10 else spam_score
        data = {
            "spam_score": contact_obj.spam_score + spam_score
        }
        serializer = MarkSpamSerializer(contact_obj, data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)