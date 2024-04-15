from django.utils import timezone
from django.db import models
from django.urls import reverse

from users.models import CustomUser


class Category(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name
  

class Tag(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name


class New(models.Model):
    class Status(models.TextChoices):
       DRAFT = "DF", "Draft"
       PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, 
                            choices=Status.choices,
                            default=Status.DRAFT)
    # view_count = models.IntegerField(default=0)
    class Meta:
        ordering = ["-publish_time"] 
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news_detail", args=[self.slug])
    

class Comment(models.Model):
   body = models.CharField(max_length=500)
   owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   commented_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f"{self.owner.username}'s comment: {self.body[:10]}"