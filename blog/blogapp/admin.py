from django.contrib import admin
from blogapp.models import Blog
# Register your models here.

#admin.site.register(Blog)

#siep1 : define  modelAdminnclass

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','details','cat','is_published','created_at']
    list_filter=('cat','is_published')
#step2:  register 

admin.site.register(Blog, BlogAdmin)