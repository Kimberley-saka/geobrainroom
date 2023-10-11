from django.db import models


class Users(models.Model):
    """
    user db model definition
    """
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=250, null=False, default='username')
    email = models.CharField(max_length=250, null=False, default='example@gmail.com')
    password = models.CharField(max_length=250, null=False)


    class Meta:
        """
        Metadata
        """
        db_table = 'users'
