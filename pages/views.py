from django.shortcuts import render
from django.views import View
from . import models


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')