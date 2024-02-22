from django.db import models


# from django.contrib.auth.models import AbstractUser
# from django.core.mail import EmailMessage
# from django.contrib.sites.shortcuts import get_current_site
# from django.conf import settings
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.template.loader import render_to_string

# class User(AbstractUser):
#     codeVarifySms = models.CharField( max_length=5,blank = True, null = True,verbose_name='کد تایید پیامکی')
#     codeVarifySmsDate = models.DateTimeField(blank = True, null = True,verbose_name='زمان تایید پیامکی')
#     # USERNAME_FIELD = 'email'

#     def create_user(self, email, username, password=None, **extra_kwargs):
#         print("kos nanat")
        

#     def save(self, *args, **kwargs):
#         print("kos nanat")
#         if self.pk:
#             # current_site = get_current_site(request)
#             print("kos nanat 1")
#             print(self.username)
#             print(self.pk)
#             print(settings.ALLOWED_HOSTS[0])

#             mail_subject = 'فعال سازی اکانت'
#             message = render_to_string('account/acc_active_email.html', {
#                 'user': self.username,
#                 'domain': settings.ALLOWED_HOSTS[0],
#                 'uid':urlsafe_base64_encode(force_bytes(self.pk)),
#                 # 'token':account_activation_token.make_token(self),
                
#             })
#         # super(User, self).save(*args, **kwargs)
#         super().save(*args, **kwargs)

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
# from common.models import CreatorBase

class CustomUserManager(BaseUserManager):
    """Custome user manager."""
    def create_user(self, email, username, password=None, **extra_kwargs):
        """Create and saves a User with the given email, username and password."""
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_kwargs):
        """Create and saves a superuser with the given email,username and password."""

        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):#, CreatorBase
    """Custom user model representing user in the system."""
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        """Return string representation of the object."""
        return self.email

    def has_perm(self, perm, obj=None):
        """Check if the user have a specific permission."""
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        """Check if the user have permissions to view the app `app_label."""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Check if the user a member of staff."""
        # Simplest possible answer: All admins are staff
        return self.is_admin