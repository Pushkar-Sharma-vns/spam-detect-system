from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from contacts.models import ContactList, SpamDatabase
from .spam_score import calculate_spam_score

User = get_user_model()

''' Whenever a user instance is created, we add that registered user data in contact list as well.'''
@receiver(post_save, sender=User)
def create_contactlist(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        phone = instance.phone
        contactlist_obj = ContactList.objects.create(name=name, phone=phone, contact_of=instance)
        # contactlist_obj.contact_of = instance
        # contactlist_obj.save()


''' Whenever a contactlist instance is created, we check its spam score and updates it, if spam_score > 50 then we add this contact in spam database.'''
@receiver(post_save, sender=ContactList)
def create_spam(sender, instance, created, **kwargs):
    if created:
        phone = instance.phone
        spam_score = calculate_spam_score(phone)
        if spam_score > 50:
            spam_obj = SpamDatabase.filter(spam_phone=phone)
            if not spam_obj:
                SpamDatabase.objects.create(spam_phone=phone)
                
        instance.spam_score = spam_score
        instance.save()
        
        