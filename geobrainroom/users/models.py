from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import check_password
from django.db import models


class UserManager(BaseUserManager):
    """
    custom user manager
    """
    def get_by_natural_key(self, username):
        """
        __summary__
        """
        return self.get(username=username)
    

    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, username
        and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


    
class Users(AbstractBaseUser):
    """
    user db model definition
    """
    username = models.CharField(max_length=250, null=False, unique=True)
    email = models.CharField(max_length=250, null=False, unique=True)
    password = models.CharField(max_length=250, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    


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
    

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
    
    class Meta:
        """
        Metadata
        """
        db_table = 'users'
