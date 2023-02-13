import os
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import openai
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.models import Info
from users.serializers import InfoSerializer
from youtubesearchpython import VideosSearch
# Create your views here.


def get_age_group(age):
    if age:
        age = int(age)
        if age == 1:
            age = 'Children'
        elif age == 2:
            age = 'Teenagers'
        elif age == 3:
            age = ''
        elif age == 4:
            age = 'Older Adults'
    else:
        age = ''
    return age


def get_bmi(height, weight):
    if height and weight:
        height = int(height) / 100
        weight = int(weight)
        bmi = weight / (height * height)
        if bmi < 18.5:
            bmi = 'Underweight'
        elif bmi >= 18.5 and bmi < 25:
            bmi = ''
        elif bmi >= 25 and bmi < 30:
            bmi = 'Overweight'
        elif bmi >= 30:
            bmi = 'Obese'
    else:
        bmi = ''
    return bmi


def search_value(search):
    videosSearch = VideosSearch(search, limit=9, region='UK')
    result = videosSearch.result()['result']
    return result


def index(request):
    gender = request.GET.get('form1', '')
    age = request.GET.get('form2', '')
    height = request.GET.get('form3', '')
    weight = request.GET.get('form4', '')

    age = get_age_group(age)
    bmi = get_bmi(height, weight)
    search = gender + ' ' + age + ' ' + bmi + ' exercise'
    result = search_value(search)
    print(search)

    context = {
        'results': result,
        "video": True,
    }
    return render(request, 'index.html', context)


def diff_age(request):
    return render(request, 'index.html', {"diff_age_train": True, })


@api_view(['GET', 'POST'])
def api_info(request):
    if request.method == 'GET':
        info = Info.objects.all()
        serializer = InfoSerializer(info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['POST'])
def api_info_create(request):
    serializer = InfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class ApiView(APIView):

    def get(self, request):
        info = Info.objects.all()
        serializer = InfoSerializer(info, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ApiViewDetail(APIView):

    def get(self, request, pk):
        info = get_object_or_404(Info, pk=pk)
        serializer = InfoSerializer(info)
        return Response(serializer.data)

    def put(self, request, pk):
        info = get_object_or_404(Info, pk=pk)
        serializer = InfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        info = get_object_or_404(Info, pk=pk)
        info.delete()
        return Response('Item deleted')
