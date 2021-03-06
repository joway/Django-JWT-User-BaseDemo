from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone as tz
from django.utils.crypto import get_random_string

ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class UserManager(BaseUserManager):
    @staticmethod
    def make_random_password(length=10, allowed_chars=ALLOWED_CHARS):
        return get_random_string(length, allowed_chars)

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = tz.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_superuser=is_superuser, is_active=True,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

    def create_staff(self, email, password, **extra_fields):
        return self._create_user(email, password, True, False, **extra_fields)


# Create your models here.
# 创建了自定义的User,也必须要创建自定义的UserManager
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('注册邮箱', unique=True, db_index=True)
    username = models.CharField('昵称', max_length=255, db_index=True, unique=True)
    name = models.CharField('姓名', max_length=255, null=True)
    school = models.CharField('目前的学校', max_length=255, null=True)
    sex = models.BooleanField('性别', choices=((False, '男'), (True, '女')), default=False)
    birthday = models.DateField('生日', null=True)
    score = models.IntegerField('积分', default=0)

    avatar = models.CharField('头像', max_length=255, blank=True, null=True)
    is_staff = models.BooleanField('管理员', default=False)
    is_active = models.BooleanField('当前状态', default=True)
    date_joined = models.DateTimeField('创建时间', default=tz.now)
    subscribed = models.BooleanField('订阅', default=True)
    verification_code = models.CharField('验证码', max_length=255, blank=True, null=True)
    expire = models.DateTimeField('验证码失效时间', blank=True, null=True)
    is_activated = models.BooleanField('是否激活', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # '-' 表示倒序
    class Meta:
        ordering = ['-id']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username
