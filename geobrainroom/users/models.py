from django.db import models


class Users(models.Model):
    """
    user db model definition
    """
    username = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=250, null=False)


    class Meta:
        """
        Metadata
        """
        db_table = 'users'
