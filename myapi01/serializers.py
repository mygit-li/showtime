#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = '无名小妖'
from rest_framework import serializers
from myapi01.models import Students


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('ic_code', 'name', 'sex', 'create_time')
