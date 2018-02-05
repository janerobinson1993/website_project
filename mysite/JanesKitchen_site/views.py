from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import BlogPost

NUMBER_OF_ROWS = 5

def index(request):

    latest_post_list = BlogPost.objects.order_by('publication_date')[:NUMBER_OF_ROWS*3]
    rows = []
    row = []
    for post in latest_post_list:
        #print(post)
        print(len(row))
        if len(row) < 3:
            row.append(post)
            print(row)
        else:
            rows.append(row)
            row = []
            row.append(post)
    # Append final row
    rows.append(row)
    print(rows)
    return render(request, 'JanesKitchen_site/index.html', {'rows': rows})


def post(request, blogpost_id):
    main_post = BlogPost.objects.get(id=blogpost_id)

    recent_articles = BlogPost.objects.order_by('publication_date').exclude(id=blogpost_id)[:3]
    rows = []
    row = []
    for post in recent_articles:
        if len(row) < 3:
            row.append(post)
        else:
            rows.append(row)
            row = []
            row.append(post)
    # Append final row
    rows.append(row)
    return render(request, 'JanesKitchen_site/post.html', {'post': main_post, 'rows': rows})

