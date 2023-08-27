from django.contrib import admin
from .models import Posts, PostComments, PostRatings, Complaints


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'date_time', 'is_moderate')
    list_editable = ('is_moderate', )
    list_filter = ('title', 'description', 'author', 'date_time', 'is_moderate')


@admin.register(PostComments)
class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'text', 'author', 'date_time')
    list_filter = ('post_id', 'text', 'author', 'date_time')


@admin.register(PostRatings)
class PostRatingsAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'status')
    list_filter = ('post', 'author', 'status')

@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('post', 'title', 'description', 'date_time')
    list_filter = ('post', 'title', 'description', 'date_time')



