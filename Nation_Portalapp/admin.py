from django.contrib import admin
from  .models import Post
# Register your models here.

class  PostModelAdmin(admin.ModelAdmin):
    list_display = ['issue','update','time']
    list_display_links = ['update']
    list_editable = ['issue']
    list_filter = ['update','time']
    search_fields = ['issue','complaint']

    class Meta:
        model=Post

admin.site.register(Post,PostModelAdmin)