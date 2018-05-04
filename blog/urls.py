from django.urls import path
from django.conf.urls import url

from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('^about/', views.AboutPageView.as_view(), name='about'),
    url(r'^about', 
        TemplateView.as_view(template_name='about.html'),
        name='about'),

]

