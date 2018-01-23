
#ere we're importing Django's function url and all of our views from the blog application
from django.conf.urls import url

from . import views

#we're now assigning a view called post_list to the ^$ URL

urlpatterns =[
    url(r'^$', views.post_list, name='post_list'),
    #views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
    #name='post_list', is the name of the URL that will be used to identify the view.
]
