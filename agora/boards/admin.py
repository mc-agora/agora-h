from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at',)

admin.site.register(Board, BoardAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'created_at', 'updated_at',)

admin.site.register(Comment, CommentAdmin)

