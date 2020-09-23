from django.conf.urls import url

from . import views

#app?機能毎のルーティング設定を行うファイル。自分で作成する。

urlpatterns = [url(r'^$', views.index, name='index')]
