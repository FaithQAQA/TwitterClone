from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile , Meep, Reply
# Register your models here.
admin.site.unregister(Group)



#mix profile info into user info
class ProfileIncline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileIncline]
    
    
    
    
admin.site.unregister(User)
    
admin.site.register(User, UserAdmin)

admin.site.register(Meep)

admin.site.register(Reply)

