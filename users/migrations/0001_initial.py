# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='注册邮箱')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='昵称')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='姓名')),
                ('sex', models.BooleanField(choices=[(False, '男'), (True, '女')], default=False, verbose_name='性别')),
                ('birthday', models.DateField(null=True, verbose_name='生日')),
                ('score', models.IntegerField(default=0, verbose_name='积分')),
                ('avatar', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('is_staff', models.BooleanField(default=False, verbose_name='管理员')),
                ('is_active', models.BooleanField(default=True, verbose_name='当前状态')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('subscribed', models.BooleanField(default=True, verbose_name='订阅')),
                ('verification_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='验证码')),
                ('expire', models.DateTimeField(blank=True, null=True, verbose_name='验证码失效时间')),
                ('is_activated', models.BooleanField(default=False, verbose_name='是否激活')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
