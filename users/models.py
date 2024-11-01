from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    pass
def __repr__(self):
    return f"User(id={self.id}, username='{self.username}', email='{self.email}')"
