from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name ='photos'


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]