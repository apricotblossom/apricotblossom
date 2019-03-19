from django.contrib import admin
from rango.models import Category, Page, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class PageAdmin(admin.ModelAdmin):
    list_display = ( 'category','evaluation', 'message')

class CategoryAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug':('name',)}


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Category,CategoryAdmin) 
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
# Register your models here.
