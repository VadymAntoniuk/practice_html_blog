from django.urls import path, re_path
from .views import HomeView, ArticleDetailView, \
    AddPostView, UpdatePostView, AboutView, DeletePostView, SearchResultsView

from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    # path('search', views.search, name='search'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('about/', AboutView.as_view(), name='about')
]
