from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import CategoryListView, CategoryDetailView


urlpatterns = [
    #url(r'^$','blog.views.home', name = "home"),
    url(r'^$', CategoryListView.as_view(), name = 'categories'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name = 'category_detail'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name = 'product_detail_function'),
    
    
]  