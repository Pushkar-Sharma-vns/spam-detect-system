from django.db import models

from account.models import User, TimeStamped


class ContactList(TimeStamped):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    spam_score = models.IntegerField(default=0)
    contact_of = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.name} {self.phone}'
    
    @property
    def is_spam(self):
        if self.spam_count > 50:
            return True
        return False
    
    
class SpamDatabase(models.Model):
    spam_phone = models.CharField(max_length=30, null=True, unique=True)
    spam_countries_code = models.CharField(max_length=10, null=True, unique=True)