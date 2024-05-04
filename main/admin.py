from django.contrib import admin
from .models import Blog, MainHeroSectionImage, NewMajorOutreach, NewsAndUpdate, VolunteerContact

# Register your models here.


admin.site.site_header = "Abby Cares Foundation Admin"
admin.site.site_title = "Welcome to Abby Cares Foundation"
admin.site.index_title = "Abby Cares Foundation"


class VolunteerContactAdmin(admin.ModelAdmin):
     list_display = ["first_name", "last_name", "phone_number", "email"]



admin.site.register(Blog)
admin.site.register(MainHeroSectionImage)
admin.site.register(NewMajorOutreach)
admin.site.register(NewsAndUpdate)
admin.site.register(VolunteerContact, VolunteerContactAdmin)
