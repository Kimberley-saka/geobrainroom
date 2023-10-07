"""
Here we authenticate a user
"""
from models import User
import bcrypt
from django.core.exceptions import ObjectDoesNotExist



def password_hash(password: str) -> bytes:
    """
    generate password hash
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

class Auth:
    """
    Authentication class
    """

    def __init__(self) -> None:
        """
        create a user object
        """
        self.users = User()
    
    def register_user(self, password: str, username: str, email: str) -> User:
        """
        register new user
        """
        if not password or not username or not email:
            return
        
        try:
            existing_user = self.users.get(email=email)
            if existing_user is not None:
                return ValueError(f'user {email} already exists')
        except ObjectDoesNotExist:
            hashed_password = password_hash(password)
            new_user = self.users(username, email, hashed_password)
            return new_user
        


