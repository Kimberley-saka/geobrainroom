from django.db import models


class User(models.Model):
    """
    A model of user student
    """
    id = models.AutoField(serialize = False, primary_key = True)
    username = models.CharField(max_length = 250, serialize = True)
    email = models.CharField(max_length = 250, null=False, serialize = True)
    password = models.CharField(max_length = 250, null = False)
    session_id = models.CharField(max_length = 250, null = False)
    

    class Meta:
        db_table = 'users'
        ordering = ['lastname']

    
     