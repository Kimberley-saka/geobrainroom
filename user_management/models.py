from django.db import models
import bcrypt

# Create your models here.
class User(models.Model):
    """
    A model of user student
    """
    id = models.AutoField(serialize = False, primary_key = True)
    firstname = models.CharField(max_length = 250, serialize = True)
    lastname =models.CharField(max_length = 250, serialize = True )
    email = models.CharField(max_length = 250, null=False, serialize = True)
    password = models.CharField(max_length = 250, null = False)
    session_id = models.CharField(max_length = 250, null = False)


    def password_hash(self, password: str) -> bytes:
        """
        generate password hash
        """
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return password_hash
    

    class Meta:
        db_table = 'users'
        ordering = ['lastname']

    
     