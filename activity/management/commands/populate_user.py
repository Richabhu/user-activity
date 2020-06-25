from django.core.management.base import BaseCommand, CommandError

from core.models import User


class Command(BaseCommand):
    help = 'Add Superuser '

    def handle(self, *args, **options):
        User.objects.create_superuser(username="Egon Spengler", first_name="Egon", last_name="Spengler",
                                      user_id="W012A3CDE", timestamp="America/Los_Angeles")
        User.objects.create_superuser(username="Glinda Southgood", first_name="Glinda", last_name="Southgood",
                                      user_id="W07QCRPA4", timestamp="Asia/Kolkata")
        return "True"
