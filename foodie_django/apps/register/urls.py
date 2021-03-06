from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^loginPage$', views.loginPage),
    url(r'^viewProduct$', views.viewProduct),
    url(r'^viewProduct/(?P<product_id>\d+)/$', views.viewProduct),
    url(r'^logout$', views.logout),
]
