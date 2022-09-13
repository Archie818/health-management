from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.models import Info
from users.serializers import InfoSerializer
# Create your views here.


def index(request):
    # Info.objects.create(name='John', age=20)
    context = {
        'title': [0]*9,
        'info': Info.objects.all()
    }
    # return render(request, 'users/index.html', context)
    return render(request, 'index.html', context)


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
    # info = Info.objects.all()
    # serializer = InfoSerializer(info, many=True)
    # return Response(serializer.data)


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

    # def post(self, request, pk):
    #     info = get_object_or_404(Info, pk=pk)
    #     serializer = InfoSerializer(info, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

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