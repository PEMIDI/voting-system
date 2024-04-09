# Generated by Django 4.2 on 2024-04-09 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'db_table': 'article',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('score', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, verbose_name='score')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='app.article', verbose_name='article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL, verbose_name='user voted')),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
                'db_table': 'votes',
                'unique_together': {('user', 'article')},
            },
        ),
    ]