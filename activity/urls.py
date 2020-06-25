from django.urls import include, path
from rest_framework import routers

from activity.views import UserTrackingView

router_user = routers.DefaultRouter()
router_user.register('tracker', UserTrackingView)  # user sign up

urlpatterns = [
    path('', include(router_user.urls)),
]
