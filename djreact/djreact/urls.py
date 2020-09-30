
from django.contrib import admin
from django.urls import path, include

# added for email reg setup
# import emailsignup.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('non-admin/', include('rest_framework.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('articles.api.urls')),

]
