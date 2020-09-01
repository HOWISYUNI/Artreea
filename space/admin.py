from django.contrib import admin

from space.models import Company,CompanyLike, CompanyType
from space.models import Equipments
from space.models import RoomEquipments, Room, RoomReview, RoomLike

# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyLike)
admin.site.register(CompanyType)

admin.site.register(Equipments)

admin.site.register(Room)
admin.site.register(RoomEquipments)
admin.site.register(RoomReview)
admin.site.register(RoomLike)