from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

#Unregistering Models
admin.site.unregister(Group)

#Mix Profile Info
class ProfileInline(admin.StackedInline):
    model = Profile

#Extending User Modal
class UserAdmin(admin.ModelAdmin):
    model = User
    fields =["username", "first_name", "last_name", "email", "is_staff", "is_active"]
    inlines = [ProfileInline]

#Unregistering Initial User
admin.site.unregister(User)

#Reregister User and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)