from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView

from activity.models import UserActivity
from activity.serializers import UserActivitySerializer


class UserTrackingView(viewsets.ModelViewSet):
    serializer_class = UserActivitySerializer
    queryset = UserActivity.objects.all()
    lookup_field = 'user'

    @action(detail=False, methods=['GET'], url_name='detail', url_path='detail')
    def activity_tracker(self, request):
        return Response("dd")
