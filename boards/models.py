#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: zhao
@contact: zhaoxinjie2016@gmail.com
@software:  
@file: models.py 
@time: 2018/6/12
"""
from django.db import models
from django.contrib.auth.models import User


# 板块的模型 !!!! 注意模型之间间隔两行
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 话题的模型，外键与板块和用户相连
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


#   django2.0之后,外键需要增加on_delete属性,否则报错


# 帖子的模型，外键与话题，用户相连
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
