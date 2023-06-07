from django.contrib import admin
from blog.models import Posts, Comments

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'user', 'photo']
    list_filter = ('is_published', )

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post_id', 'post', 'date']
