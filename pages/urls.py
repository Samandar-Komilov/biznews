from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('news/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('categories/<str:category>/', views.CategoryView.as_view(), name='category'),
    path('search-results/', views.SearchResultsList.as_view(), name='search_results'),
    # Auth
    path('signup/', views.SignUpView.as_view(), name='register'),
    # 3rd party
    path('contact/', views.ContactView.as_view(), name='contact'),
]
