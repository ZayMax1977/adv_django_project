from django.contrib import admin

from posts.models import Category
from posts.views import PostList


class PostListAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','published','city','author',)
    list_display_links = ('title',)
    search_fields = ('title','rubric','author',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

# class LikesAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)
#     search_fields = ('name',)

admin.site.register(PostList,PostListAdmin)
admin.site.register(Category,CategoryAdmin)
# admin.site.register(Likes,LikesAdmin)

