from django.contrib import admin
from .models import BlogPost, Comment, Profile
from django_summernote.admin  import SummernoteModelAdmin




@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'updated_on')
    list_display = ('title', 'slug', 'status', 'updated_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'published_on', 'approved')
    list_filter = ('approved', 'published_on')
    search_fields = ['name', 'email', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    search_fields = ['user', 'email', 'bio']
    list_display = ['user', 'bio']
    list_filter = ['user', 'bio']



