from django.db import models


class Users(models.Model):
    """
    user db model definition
    """
    username = models.CharField(max_length=250, null=False, unique=True)
    email = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=250, null=False)


    REQUIRED_FIELDS = [ 'email', 'password']
    USERNAME_FIELD = 'username'

    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True

    class Meta:
        """
        Metadata
        """
        db_table = 'users'
