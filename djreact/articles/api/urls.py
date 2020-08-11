from django.urls import path

from .views import ArticleListView, ArticleDetailView

# the <pk> path allows articles/1, have seen other examples, but this is more specific

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view())
]