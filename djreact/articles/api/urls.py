from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

#when viewing create have to put in base/api/create/ bc of / below

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('<pk>/update/', ArticleUpdateView.as_view()),
    path('<pk>/delete/', ArticleDeleteView.as_view())
]