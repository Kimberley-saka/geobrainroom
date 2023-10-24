from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import check_password


class UserManager(BaseUserManager):
    """
    custom user manager
    """
    def get_by_natural_key(self, username):
        """
        __summary__
        """
        return self.get(username=username)
    
    def create_user(self, email, password=None, **kwargs):
        """
        Create and return a regular user with an email and password
        """
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        # Create and return a superuser with an email and password
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **kwargs)
    
class Users(models.Model):
    """
    user db model definition
    """
    username = models.CharField(max_length=250, null=False, unique=True)
    email = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=250, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    


    REQUIRED_FIELDS = [ 'email', 'password']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def check_password(self, raw_password):
        """
        check password
        """
        return check_password(raw_password, self.password)
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True
    

    def get_by_natural_key(self, username):
        return self.get(username=username)
    
    class Meta:
        """
        Metadata
        """
        db_table = 'users'
