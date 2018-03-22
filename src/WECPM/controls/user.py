#!/usr/bin/env python
# coding:utf-8
# author:john
"""
User控制类
"""
from django.shortcuts import render
from WECPM.models import User


def index(request):
    '''user列表'''
    content = {}

    return render(request, "user.html", content)
