from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.dispatch import receiver
from django.urls import reverse

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    username = None
    name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    activation_code = models.CharField(max_length=50, blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    def create_activation_code(self):
        import uuid

        code = str(uuid.uuid4())
        self.activation_code = code

class ResetPassword(models.Model):
    email = models.EmailField()
    key = models.CharField(max_length=50, blank=True)

    def create_activation_code(self):
        import uuid

        code = str(uuid.uuid4())
        self.key = code


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        f'перейдите по этому пути и введите новый пароль и токен:\nhttp://localhost:8000/account/password_reset/confirm/ \n{reset_password_token.key}',
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )