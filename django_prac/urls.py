"""django_prac URL Configuration

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
from django.urls import path, include, re_path
from posts import views

#写真の表示に必要
from django.conf.urls.static import static
from django.conf import settings

##PJ全体でのルーティング設定

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    re_path('posts/(?P<post_id>[0-9]+)/$', views.post_detail, name="post_detail")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)　→　メディア（写真）の表示で使用
# settings.pyの修正も合わせて必要