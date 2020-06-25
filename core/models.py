from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractUser):
    """
    Abstract model for User.
    """
    username = models.CharField(max_length=50, unique=True)
    user_id = models.CharField(_('user_id'), unique=True, max_length=50)
    timestamp = models.CharField(_('timestamp'), max_length=50)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_id', 'timestamp']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
