from django.conf.urls import url

from . import views

"""account.urls"""
urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^signup/$',views.signup),
    # url(r'^isLogin/$',views.isLogin),
    # url(r'^info/$',views.info),
    # url(r'^logout/$',views.logout),
]
