from django.shortcuts import redirect, render
from django.views import View, generic
from django.db.models import Q
from . import models
from . import forms

from django.contrib import messages


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


class CategoryView(View):
    def get(self, request, category):
        category_object = models.Category.objects.get(name=category)
        category_news = models.New.published.filter(category = category_object)
        context = {
            'category_news': category_news,
            'category': category,
        }
        return render(request, "category.html", context=context)


class PostDetailView(View):
    def get(self, request, slug):
        all_news = models.New.published.all().order_by("-publish_time")
        new = models.New.published.get(slug=slug)
        comments = models.Comment.objects.filter(post=new).order_by("commented_at")
        comment_num = comments.count()
        breaking_news = all_news[4:7]
        context = {
            "new": new,
            'breaking_news': breaking_news,
            'comments': comments,
            'comment_num': comment_num,
        }
        return render(request, "detail.html", context=context)
    

# Auth system

class SignUpView(View):
    def get(self, request):
        return render(request, "auth/signup.html")
    def post(self, request):
        user_form = forms.SignUpForm(request.POST)
        email_test = user_form['email']
        if models.CustomUser.objects.get(email=email_test):
            messages.error("This email has already been signed up!")
            render(request, "auth/signup.html")
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.is_active = False
            new_user.save()

            context = {
                'new_user': new_user,
            }
            return render(request, "auth/email_confirm.html", context=context)
        else:
            # Handle form validation errors
            for field, errors in user_form.errors.items():
                for error in errors:
                    if field == 'password':
                        # Handle password-related errors
                        if 'min_length' in error:
                            messages.error(request, "Password must contain at least 8 characters.")
                        elif 'required' in error:
                            messages.error(request, "Please enter a password.")
                        # Add more conditions as needed for other password-related errors
                    elif field == 'email':
                        # Handle email-related errors
                        if 'invalid' in error:
                            messages.error(request, "Please enter a valid email address.")
                        # Add more conditions as needed for other email-related errors
                    # Add more conditions as needed for other fields

            return render(request, "auth/signup.html")


# 3rd Party

class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")
    def post(self, request):
        form = forms.ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            messages.error(request, "Please enter your credentials correctly!")
            return render(request, "contact.html")
            
            
    

# Search news

class SearchResultsList(View):
    def get_queryset(self):
        query = self.request.GET.get('q')
        return models.New.published.filter(
            Q(title__icontains = query) | Q(subtitle__icontains = query)
        )
    
    def get(self, request):
        results = self.get_queryset()
        context = {
            "searched_news": results
        }
        print(results)
        return render(request, "search-results.html", context=context)