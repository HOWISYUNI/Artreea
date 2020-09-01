from django.db import models

# Create your models here.

#TODO MYSQL 연동 후 각 클래스마다 내부클래스(class Meta)로 테이블 명시

class User(models.Model):

    # Field
    name              = models.CharField(max_length = 45)
    email             = models.EmailField(max_length = 100, unique = True)
    password          = models.CharField(max_length = 100, null = True)
    phone_number      = models.CharField(max_length = 13, unique = True)
    social_login_type = models.ForeignKey('SocialLoginType', on_delete = models.SET_NULL, null = True)
    social_login_id   = models.CharField(max_length = 45, null = True)
    create_at         = models.DateTimeField(auto_now_add = True)
    update_at         = models.DateTimeField(auto_now = True)


class SocialLoginType(models.Model):
    name = models.CharField(max_length=20)


class Owner(models.Model):

    # Field
    name            = models.CharField(max_length = 10)
    face_name       = models.CharField(max_length = 10)
    face_number     = models.CharField(max_length = 13)
    business_id     = models.CharField(max_length = 12)
    created_at      = models.DateTimeField(auto_now_add = True)