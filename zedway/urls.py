"""zedway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from accounts.views import ActivateAccount
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls
from home.views import delete_notifs

urlpatterns = [
    path('', include(('home.urls', 'home'), namespace='home')),
    path('admin/', admin.site.urls),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('allauth.urls')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('notifications/', include(notifications.urls, namespace='notifications')),
    path('notifications/delete/', delete_notifs, name='delete-notifs'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
