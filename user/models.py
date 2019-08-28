from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
)
import jwt
import random
import string
from datetime import datetime, timedelta
from django.conf import settings

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username = None
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    access_token = models.CharField(max_length=255, null=False)
    refresh_token = models.CharField(max_length=255, null=False)
    is_login = models.BooleanField(default=False)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # objects = UserManager()
    def create(self, **kwargs):
        """Create and return a `User` with an email, username and password."""
        
        user = User(email=self.normalize_email(kwargs['email']), first_name=kwargs['first_name'],\
                last_name=kwargs['last_name'])
        user.save()
        return user

    objects = UserManager()


    def __str__(self):
        return self.email 
    
    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        # dt = datetime.now() + timedelta(days=60)
        dt = datetime.now() + timedelta(minutes=2)
        token = jwt.encode({
            'id': self.id,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        # dt = datetime.now() + timedelta(days=60)
        dt = datetime.now() + timedelta(minutes=2)
        token = jwt.encode({
            'id': self.id,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


class Story(models.Model):
    name = models.CharField(max_length=30)

class StoryPage(models.Model):
    story = models.ForeignKey(Story,  related_name="inputs", on_delete=models.CASCADE)
    page_name = models.CharField(max_length=30)


class StoryPageLocation(models.Model):
    StoryPage = models.ForeignKey(StoryPage,  related_name="inputs", on_delete=models.CASCADE)
    page_name = models.CharField(max_length=30)
