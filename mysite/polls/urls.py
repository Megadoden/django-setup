from django.conf.urls import url
from . import views

# Map the index view to the index url.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]
