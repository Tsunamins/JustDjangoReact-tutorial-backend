from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from articles.models import Article
from .serializers import ArticleSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )

#previous version when auths not needed:
#shorter viewsets will also show a create/update/and delete view available in /api

# from rest_framework import viewsets

# from articles.models import Article
# from .serializers import ArticleSerializer

# class ArticleViewSet(viewsets.ModelViewSet):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()