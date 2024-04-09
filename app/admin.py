from django.contrib import admin
from .models import Article, Vote


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'score', 'created_at')
    search_fields = ('user__username', 'article__title')
    ordering = ('-created_at',)
