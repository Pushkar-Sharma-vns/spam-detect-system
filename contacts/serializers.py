from rest_framework import serializers

from . models import ContactList
from account.models import User


class ContactListSerializer(serializers.ModelSerializer):
    spam_likelihood = serializers.SerializerMethodField()
    # email = serializers.SerializerMethodField()
    # user = serializers.SerializerMethodField()
    
    class Meta:
        model = ContactList
        fields = ["name", "phone", "spam_score", "spam_likelihood"]
        
    def get_spam_likelihood(self, obj):
        spam_score = obj.spam_score
        if spam_score >= 50:
            return "!!Very likely to be a spam contact!!"
        elif spam_score >= 25 and spam_score < 50:
            return "Likely to be a spam contact!!"
        elif spam_score >=10 and spam_score <25:
            return "Can be a spam contact!"
        return "Not a spam contact."
    
    # def get_user(self, obj):
    #     user = self.context.get('user', None)
    #     return user
         
    # def get_email(self, obj):
    #     phone = obj.phone
    #     person_in_user_contactlist = True if self.user == obj.contact_of else False
    #     person_is_registered = True if User.objects.get(phone=phone) else False
    #     if person_in_user_contactlist and person_is_registered:
    #         return self.user.email
    #     return "No permissions to view this user's email."
        

        
class MarkSpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactList
        fields = ["spam_score"]
