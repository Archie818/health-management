from rest_framework import serializers
from users.models import Info


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ('id', 'name', 'age')

# get video from youtube
class GetVideoSerializer(serializers.Serializer):
    gender = serializers.CharField()
    age = serializers.IntegerField()
    height = serializers.IntegerField()
    weight = serializers.IntegerField()