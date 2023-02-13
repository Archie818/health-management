from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from youtubesearchpython import VideosSearch

from api.serializers import GetVideoSerializer
from users.views import get_bmi, search_value

# Create your views here.

def api(request):
    return render(request, 'index.html', { "api": True,})

def get_age_group(age):
	if age < 5:
		age = 'Children'
	elif age >= 5 and age < 19:
		age = 'Teenagers'
	elif age >= 19 and age < 65:
		age = 'Adults'
	elif age >= 65:
		age = 'Older Adults'
	return age

# get video from youtube api
class GetVideo(APIView):
    serializer_class = GetVideoSerializer

    def get(self, request):
        search = 'exercise'
        result = search_value(search)
        return Response(result)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            json_data = serializer.data
            gender = json_data.get("gender", "")
            if gender.upper() not in ['MALE', 'FEMALE']:
                return Response({'error': 'Must enter one of male or female'})
            age = json_data.get("age", "")
            age = get_age_group(age)
            height = json_data.get("height", "")
            weight = json_data.get("weight", "")
            bmi = get_bmi(height, weight)
            search = gender + age + bmi + 'exercise'
            result = search_value(search)
            return Response(result)
        else:
            return Response(serializer.errors)