from django.contrib import admin
from .models import Blog, MainHeroSectionImage, NewMajorOutreach, NewsAndUpdate

# Register your models here.



admin.site.register(Blog)
admin.site.register(MainHeroSectionImage)
admin.site.register(NewMajorOutreach)
admin.site.register(NewsAndUpdate)