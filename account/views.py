from django.http.response import JsonResponse,HttpResponse
from zjupinche.decorators import json_request
from . import zjuAuth
from .models import *
import django.contrib.auth as auth
from zjupinche.tools import GeneralResponse


@json_request
def login(request):
    # TODO
    # request.json['studentId']
    # request.json['password']
    return GeneralResponse()


@json_request
def signup(request):
    if not zjuAuth.auth(request.json['studentId'],request.json['password']):
        return GeneralResponse(False,'认证失败')
    user=User.objects.create_user(
        username=request.json['studentId'],
        password=request.json['password'],
        nickName=request.json['nickName'],
        gender=request.json['gender'],
        phone=request.json['phone'],
        weChat=request.json['weChat']
    )
    user.save()
    auth.login(request, user)
    return GeneralResponse()


