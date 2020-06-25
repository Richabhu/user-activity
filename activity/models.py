from django.db import models


# Create your models here.
from core.models import User


class UserActivity(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.user, self.start_time, self.end_time)

    class Meta:
        db_table = "user_activity"
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"
