from rest_framework import serializers

from activity.models import UserActivity


class UserActivitySerializer(serializers.ModelSerializer):
    """
    Serializer class for Product Permission
    """

    class Meta:
        """
        Customized fields for product permission
        """
        model = UserActivity
        exclude = ('id',)
