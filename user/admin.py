from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'mobile_number')
    list_filter = ('is_staff',)
    search_fields = ('email', 'mobile_number')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'email',
                    'mobile_number',
                    'user_permissions',
                    'groups',
                    'password',
                )
            },
        ),
        (
            'Permissions',
            {'fields': ('is_staff',)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'name',
                    'email',
                    'mobile_number',
                    'groups',
                    'password1',
                    'password2',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
