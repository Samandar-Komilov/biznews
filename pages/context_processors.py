from django.utils import timezone
from . import models

def current_datetime(request):
    return {"current_datetime": timezone.now()}

def categories(request):
    all_categories = models.Category.objects.all()
    top_categories = models.Category.objects.all().order_by('id')[:3]
    dropdown_categories = models.Category.objects.all().order_by('id')[3:]
    context = {
        "all_categories": all_categories,
        "top_categories": top_categories,
        "dropdown_categories": dropdown_categories,
    }
    return context

def tags(request):
    all_tags = models.Tag.objects.all()
    context = {
        "all_tags":all_tags,
    }
    return context