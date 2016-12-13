from django.conf.urls import url
from . import views

ap_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'), # Index URL
    ]
