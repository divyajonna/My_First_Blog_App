# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

#creating post_list view
def post_list(request):
    return render(request, 'blog1/post_list.html',{})
    #render (put together) our template blog/post_list.html.
