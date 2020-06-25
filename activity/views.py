import datetime
from dateutil import parser

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
from rest_framework.utils import json
from rest_framework.views import APIView

from activity.models import UserActivity
from activity.serializers import UserActivitySerializer
from core.models import User


class UserTrackingView(viewsets.ModelViewSet):
    serializer_class = UserActivitySerializer
    queryset = UserActivity.objects.all()
    lookup_field = 'user'

    @action(detail=False, methods=['GET'], url_name='detail', url_path='detail')
    def activity_tracker(self, request):
        res = dict()
        res['ok'] = True
        members = list()
        user = User.objects.all()
        all_tracker = self.queryset
        kk = list

        for _each_user in user:
            each_user_res = dict()
            if _each_user in list_user_activity(all_tracker):
                each_user_res['id'] = _each_user.user_id
                each_user_res['real_name'] = "{} {}".format(_each_user.first_name, _each_user.last_name)
                each_user_res['tz'] = _each_user.timestamp
                activity_res = list()

                for _each_tracker in all_tracker:
                    if _each_tracker.user == _each_user:  # tracker == user
                        _each_user_tracker = dict()
                        _start_time = parser.parse(str(_each_tracker.start_time))
                        _each_user_tracker['start_time'] = _start_time.strftime('%B %d %Y %I:%M %p')
                        _each_user_tracker['end_time'] = _each_tracker.end_time #.strftime('%B %d %Y %I:%M %p')
                        activity_res.append(_each_user_tracker)
                each_user_res['activity_periods'] = activity_res
                members.append(each_user_res)
        res['members'] = members
        print(res)
        return Response(res)


def list_user_activity(all_activity):
    """
    This fn returns list of users whose activity is done
    :param all_activity:
    :return:
    """
    users = set()
    for info in all_activity:
        users.add(info.user)
    return users
