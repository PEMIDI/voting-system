
from django.contrib import admin
from django.urls import path, include

from app.views import VoteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('vote/', VoteView.as_view(), name='vote')
]
