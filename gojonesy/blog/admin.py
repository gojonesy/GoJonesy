from django.contrib import admin

# Register your models here.
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'lastUpdate')
    list_filter = ['lastUpdate', 'timestamp']
    search_fields = ['title', 'content']
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
