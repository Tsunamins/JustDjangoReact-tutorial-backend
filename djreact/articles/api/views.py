#change method for basic, unauthed get, put, patch, destroy requests
#uses less lines of code, keeping the other version for use when auths get involved in tutorial
#this part stays thes same
from articles.models import Article
from .serializers import ArticleSerializer

#methods below, instead, to use all views in one
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer


#this part is for permissions used later and not necc as viewsets currently stands
#from rest_framework import permissions

#this is from the method used later for auths
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )

#methods below using each specific type of View
# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (permissions.AllowAny, )


# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (permissions.AllowAny, )


# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (permissions.IsAuthenticated, )