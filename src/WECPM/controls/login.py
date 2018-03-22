#!/usr/bin/env python
# coding:utf-8
# author:john
"""
登录
"""
import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings


def index(request):
    """
    登录初始页面
    :param request:
    :return:
    """
    content = {
        "title": settings.APP_NAME,
        "copyright": datetime.datetime.now().year,
    }
    return render(request, "login.html", content)


def verifycode(requset):
    """
    获取验证码及图片
    :param requset:
    :return:
    """
    import WECPM.common.verifycode as vc
    verify = vc.VerifyCode()
    code = verify.get_verify_code(length=4)
    imgbuffer = verify.get_verify_img(code)
    return HttpResponse(imgbuffer.getvalue(), content_type='image/png')


def check(requset):
    """
    ajax登陆验证
    :param requset:
    :return:
    """
    # data = json.load(requset.body)
    response = {
        "code": 100,
        "msg": "Get success",
        # "account": data["code"],
    }
    # return HttpResponse(json.dumps(response), content_type="application/json")
    return JsonResponse(response)
