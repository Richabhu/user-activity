from django.contrib import admin

# Register your models here.
from activity.models import UserActivity

admin.site.register(UserActivity)