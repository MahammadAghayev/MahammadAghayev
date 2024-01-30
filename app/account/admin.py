from django.contrib import admin
from .models import Account, SubscribedUser
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'get_full_name')


admin.site.register(SubscribedUser)