from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from articles.models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, CreateUserSerializer
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class CreateUserView(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(username=user_data['username'])
        current_site = get_current_site(request).domain
        # add later based on a login url
        # relativeLink = reverse('')
        absurl = 'http://' + current_site
        message = 'Welcome ' + user.username + ', click the link below to begin the writing on The Wall. \n' + absurl
        data = {'message': message, 'to': user.email}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


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
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def complete_view(request):
    return Response("Email account is activated")
