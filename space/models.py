from django.db import models

from account.models import User,Owner

#TODO MYSQL 연동 후 각 클래스마다 내부클래스(class Meta)로 테이블 명시
#TODO RoomReview 사용자 permission
#TODO ADD image url field

# Create your models here.

class CompanyType(models.Model):
    """Model related to Company.company_type(공연장, 연습실..)"""

    # Field
    name = models.CharField(max_length=10)


class CompanyLike(models.Model):

    # Field
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    user    = models.ForeignKey('account.User', on_delete=models.CASCADE)


class Company(models.Model):
    """ Model representing Company"""

    # Field
    name            = models.CharField(max_length=45)
    owner           = models.ForeignKey('account.Owner', on_delete=models.SET_NULL, null=True)
    summary         = models.TextField(max_length=1000, null=True)
    jibun_address   = models.CharField(max_length=45, null=True)
    road_address    = models.CharField(max_length=45,null=True)
    company_type    = models.ForeignKey('CompanyType', on_delete=models.SET_NULL, null=True)
    longitude       = models.DecimalField(max_digits=20, decimal_places=15, default=0.0) # non-nullable 에러를 피하기위해 default값을 설정하거나 null=true를 설정해야한다.
    latitude        = models.DecimalField(max_digits=20, decimal_places=15, default=0.0)
    company_reviews = models.ManyToManyField(User, through='RoomReview', related_name='company_review_set') # ORM 동작원리에 따라 동일한 모델(User)을 참조하면 Reverse accessor error(fields.E304)가 발생하므로 related_name을 명시적으로 지정해줘야한다.
    company_like    = models.ManyToManyField(User, through='CompanyLike', related_name='company_like_set')

    # Method
    def __str__(self):
        return self.name

class Equipments(models.Model):
    
    # Field
    name = models.CharField(max_length=45)


class RoomEquipments(models.Model):
    
    # Field
    room        = models.ForeignKey('Room', on_delete=models.CASCADE)
    equipment   = models.ForeignKey(Equipments, on_delete=models.CASCADE)

class Room(models.Model):
    """Model representing Room which is serviced by Company """

    # Field : 사진, 이름, 가격, 공간소개, 장비현황, 예약시 주의사항, 환불/취소 규정안내
    name        = models.CharField(max_length=45)
    price       = models.PositiveIntegerField(help_text='Enter price over 0')
    summary     = models.TextField(max_length=1000, null=True)
    caution     = models.TextField(max_length=1000, null=True)
    refund_policy = models.TextField(max_length=1000, null=True)
    cancel_policy = models.TextField(max_length=1000, null=True)
    is_available  = models.BooleanField(default=False)
    company     = models.ForeignKey('Company', on_delete=models.CASCADE)
    size        = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    equipements = models.ManyToManyField(Equipments, through='RoomEquipments')
    room_reviews = models.ManyToManyField(User, through='RoomReview', related_name='room_reviews_set')
    room_like    = models.ManyToManyField(User, through='RoomLike', related_name='room_like_set')

    # Method
    def __str__(self):
        return f'{self.company.name}_{self.name}'


class RoomReview(models.Model):
    """ Model representing Review about Company by it's Users """
    # Field
    user    = models.ForeignKey('account.User', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    room    = models.ForeignKey('Room', on_delete=models.CASCADE)
    review  = models.TextField(max_length=1000)
        #user : permission 문제. 사용한 사람만 리뷰남길 수 있음.


class RoomLike(models.Model):

    # Field
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)


