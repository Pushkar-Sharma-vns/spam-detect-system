from django.utils import timezone
from django.core.validators import RegexValidator

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

phone_regex = RegexValidator(
    regex=r'^\+?\d{1,3}[-.\s]?\d{3,14}$',
    message="Phone number must be entered in a valid format."
)


class TimeStamped(models.Model):
    created_at = models.DateTimeField(editable=False, null=True)
    updated_at = models.DateTimeField(null=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)
    
    
class UserManager(BaseUserManager):
    def create_user(self, name, phone, password, **extra_fields):
        if not name or not phone or not password:
            raise ValueError("User must provide name, phone number and password.")
        
        user = self.model(name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, name, phone, password, **extra_fields):
        user = self.create_user(name=name, phone=phone, password=password)
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser, TimeStamped):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, validators=[phone_regex], db_index=True, unique=True)
    email = models.EmailField(unique=True, max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin