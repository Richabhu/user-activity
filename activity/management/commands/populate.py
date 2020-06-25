from django.core.management.base import BaseCommand, CommandError

from activity.models import UserActivity
from core.models import User


class Command(BaseCommand):
    help = 'Add user '

    def handle(self, *args, **options):
        user1 = User.objects.create_superuser(username="Egon Spenglerr", first_name="Egon", last_name="Spengler",
                                              user_id="W012A3CDER", timestamp="America/Los_Angeles", is_superuser=True)
        user2 = User.objects.create_superuser(username="Glinda Southgoodd", first_name="Glinda", last_name="Southgood",
                                              user_id="W07QCRPA4t5", timestamp="Asia/Kolkata")
        UserActivity.objects.create(start_time="2020-06-25T17:50:30Z", end_time="2020-07-25T17:50:30Z", user=user1)
        UserActivity.objects.create(start_time="2020-02-25T17:50:30Z", end_time="2020-03-25T17:50:30Z", user=user1)
        UserActivity.objects.create(start_time="2020-01-25T17:50:30Z", end_time="2020-02-25T17:50:30Z", user=user1)
        UserActivity.objects.create(start_time="2020-06-25T17:50:30Z", end_time="2020-07-25T17:50:30Z", user=user2)
        UserActivity.objects.create(start_time="2020-02-25T17:50:30Z", end_time="2020-03-25T17:50:30Z", user=user2)
        UserActivity.objects.create(start_time="2020-01-25T17:50:30Z", end_time="2020-02-25T17:50:30Z", user=user2)
        return "True"
