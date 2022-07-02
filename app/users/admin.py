from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    readonly_fields = ('date_joined',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)