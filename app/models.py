from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Count, Avg
from django.utils.translation import gettext as _

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('updated at'))

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = "Articles"
        db_table = "article"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Vote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes', verbose_name=_('user voted'))
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='votes', verbose_name=_('article'))
    score = models.SmallIntegerField(default=0, choices=[(i, i) for i in range(6)], verbose_name=_('score'))

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
        db_table = 'votes'
        unique_together = ('user', 'article')

    def __str__(self):
        return f"{self.user} voted article: {self.article.title} with score {self.score}"
