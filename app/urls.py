from django.urls import path
from .views import ArticleListView, VoteView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('vote/', VoteView.as_view(), name='vote')
]