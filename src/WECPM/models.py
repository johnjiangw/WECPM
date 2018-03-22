#!/usr/bin/env python
# coding:utf-8
# author:john
"""
description
"""
from django.db import models
from django.utils import timezone

class User(models.Model):
    '''用户实体'''
    class Meta:
        db_table = 'Sys_User'
    id = models.AutoField(db_column="ID", primary_key=True)
    user_name = models.CharField(db_column='UserName', max_length=50, blank=False)
    login_name = models.CharField(db_column='LoginName', max_length=50, blank=False)
    pwd = models.CharField(db_column='Pwd', max_length=50, blank=False)
    state = models.SmallIntegerField(db_column='State', default=1)
    last_login_time = models.DateTimeField(db_column='LastLoginTime')
    create_time = models.DateTimeField(db_column='CreateTime', default=timezone.now)
    bak = models.TextField(db_column='Bak', max_length=500)
    email = models.CharField(db_column='Email', max_length=50)
    mobile = models.CharField(db_column='Mobile', max_length=50)
