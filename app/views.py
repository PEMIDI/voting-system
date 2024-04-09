from django.db.models import Avg, Sum, Count
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Article, Vote
from .serializers import ArticleSerializer, VoteSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.prefetch_related('votes').annotate(
        average_rating=Avg('votes__score'),
        vote_count=Count('votes')
    )
    serializer_class = ArticleSerializer


class VoteView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def post(self, request, *args, **kwargs):
        article_id = request.data.get('article')
        user = request.user
        score = int(request.data.get('score'))

        existing_vote = Vote.objects.filter(article_id=article_id, user=user).first()

        if existing_vote:
            serializer = self.get_serializer(existing_vote, data={'score': score}, partial=True)
        else:
            serializer = self.get_serializer(data={'article': article_id, 'user': user.id, 'score': score})

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)