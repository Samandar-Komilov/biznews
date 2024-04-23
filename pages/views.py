from django.shortcuts import render
from django.views import View
from . import models


class HomeView(View):
    def get(self, request):
        all_news = models.New.published.all().order_by("-publish_time")
        top3_news = all_news[:3]
        last4_news = all_news.order_by('publish_time')[:4]
        breaking_news = all_news[4:7]
        latest6_news = all_news[:6]
        context = {
            "all_news": all_news,
            "top3_news": top3_news,
            "last4_news": last4_news,
            "breaking_news": breaking_news,
            "latest6_news": latest6_news,
            # "next4_news_col1": next2_news_col1,
            # "next2_news_col2": next2_news_col2,
        }
        return render(request, 'index.html', context=context)


class PostDetailView(View):
    def get(self, request, slug):
        new = models.New.published.get(slug=slug)
        context = {
            "new": new
        }
        return render(request, "detail.html", context=context)
    

class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")