from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import  JSONParser
from .serializers import CcrFormSerializer , RequestorSerializer , ActionSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from .models import TestTable , Requestor ,Action


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        Json_Data = request.body
        stream = io.BytesIO(Json_Data)
        pythondata = JSONParser().parse(stream)
        serializer = CcrFormSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            Json_Data = JSONRenderer().render(res)
            return HttpResponse(Json_Data,content_type='application/json')
        Json_Data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')  



@csrf_exempt
def CcrFormGet(request):
    stu = TestTable.objects.all()
    serializer = CcrFormSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
                


@csrf_exempt
def CcrFormGetPrimaryKey(request,pk):
    stu = TestTable.objects.get(id = pk)
    serializer = CcrFormSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def RequestorGet(request):
    stu = Requestor.objects.all()
    serializer = RequestorSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def RequestorNameGet(request,name):
    stu = Requestor.objects.get(name = name)
    serializer = RequestorSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')    

                

@csrf_exempt
def ActionCreate(request):
    if request.method == 'POST':
        Json_Data = request.body
        stream = io.BytesIO(Json_Data)
        pythondata = JSONParser().parse(stream)
        serializer = ActionSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            Json_Data = JSONRenderer().render(res)
            return HttpResponse(Json_Data,content_type='application/json')
        Json_Data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json') 


@csrf_exempt
def ActionGet(request):
    stu = Action.objects.all()
    serializer = ActionSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')        