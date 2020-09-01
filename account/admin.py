from django.contrib import admin

# Register your models here.
from django.contrib import admin
from account.models import User, SocialLoginType, Owner

# Register your models here.

admin.site.register(User)
admin.site.register(SocialLoginType)
admin.site.register(Owner)