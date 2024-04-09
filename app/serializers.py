from rest_framework import serializers
from .models import Article, Vote


class ArticleSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    vote_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'average_rating', 'vote_count']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'article', 'score']

