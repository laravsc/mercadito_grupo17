from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Extras", {"fields": ("avatar", "bio", "reputation", "phone")}),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ("Extras", {"fields": ("avatar", "bio", "reputation", "phone")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "reputation")

