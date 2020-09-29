from django.urls import path

from django.conf.urls import url, include

from . import views

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
  
)

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/create/', ArticleCreateView.as_view()),
    path('articles/<pk>', ArticleDetailView.as_view()),
    path('articles/<pk>/update/', ArticleUpdateView.as_view()),
    path('articles/<pk>/delete/', ArticleDeleteView.as_view()),
  
]

# Previous short version for when auths aren't needed:

# from articles.api.views import ArticleViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ArticleViewSet, base_name='articles')
# urlpatterns = router.urls
