from django.shortcuts import render
from django.views import View
from . import models


class HomeView(View):
    def get(self, request):
        all_news = models.New.published.all().order_by("-publish_time")
        top3_news = all_news[:3]
        last4_news = all_news.order_by('publish_time')[:4]
        breaking_news = all_news[4:7]
        latest4_news = all_news[:4]
        context = {
            "all_news": all_news,
            "top3_news": top3_news,
            "last4_news": last4_news,
            "breaking_news": breaking_news,
            "latest4_news": latest4_news
        }
        return render(request, 'index.html', context=context)