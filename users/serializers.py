from rest_framework import serializers
from users.models import Info


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ('id', 'name', 'age')
