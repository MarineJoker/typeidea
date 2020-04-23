"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

# from blog.views import post_list, post_detail
from config.views import links
from typeidea.custom_site import custom_site
from rest_framework.routers import DefaultRouter
from blog.apis import PostViewSet
from rest_framework.documentation import include_docs_urls
# from blog.apis import post_list, PostList

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-name')

urlpatterns = [
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),
    url(r'^api/', include(router.urls, namespace="api")),
    # url(r'^api/post/', post_list, name='post-list'),
    # url(r'^api/post/', PostList.as_view(), name='post-list'),
    # url(r'^$', post_list),
    # url(r'^category/(?P<category_id>\d+)/$', post_list),
    # url(r'^tag/(?P<tag_id>\d+)/$', post_list),
    # url(r'^post/(?P<post_id>\d+).html$', post_detail),
    # url(r'^links/$', links),
    url(r'^admin/', custom_site.urls),
    url(r'^superadmin/', admin.site.urls)
]
