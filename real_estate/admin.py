from django.contrib import admin
from .models import Property, Companies, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    max_num = 10
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline]
admin.site.register(Companies)




