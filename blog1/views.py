# -*- coding: utf-8 -*-

from django.shortcuts import render

#when we have to include the model we have written in models.py
from .models import Post
# . - is for current/same directory
#import the name of the model


# Create your views here.

#creating post_list view
def post_list(request):
    #we want published blog posts sorted by published_date -using query set
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # we created a variable for our QuerySet: posts

    return render(request, 'blog1/post_list.html',{'posts':posts})
    #render (put together) our template blog/post_list.html.
    #In the render function we have one parameter request (everything we receive from the user via the Internet)
        #and another giving the template file ('blog/post_list.html').
    #The last parameter, {}, is a place in which we can add some things for the template to use
