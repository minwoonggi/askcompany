from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

# Register your models here.
# 등록법 1
# admin.site.register(Post)

# 등록법 2
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 등록법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
    
    def photo_tag(self,post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" />')
        return None
    
    def message_length(self, post): # admin이 알아서 호출해주는 post
        return f"{len(post.message)} 글자"
    
# python manage.py shell
# instagram.models import Post
# Post.object.all()
# qs = Post.object.all().filter(message__icontains='글')
# print(qs.query)
# SELECT "instagram_post"."id", "instagram_post"."message", "instagram_post"."created_at", "instagram_post"."updated_at" 
# FROM "instagram_post" WHERE "instagram_post"."message" LIKE %글% ESCAPE '\'
        