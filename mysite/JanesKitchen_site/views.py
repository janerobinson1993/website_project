from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import BlogPost


def index(request):
    latest_post_list = BlogPost.objects.order_by('publication_date')[:5]
    output = ', '.join([b.title_text for b in latest_post_list])
    return HttpResponse(output)


def post(request, blogpost_id):
    output = BlogPost.objects.get(id=blogpost_id)
    return HttpResponse(output.title_text + output.body_text + str(output.publication_date))

