from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ask_app.models import *
from ask_app.forms import CreateUserForm, ChangeUserForm
from django.utils.translation import ugettext_lazy as _


class NewUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'avatar'),
        }),
    )
    form = ChangeUserForm
    add_form = CreateUserForm
    ordering = ('username',)


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tags)
admin.site.register(User, NewUserAdmin)