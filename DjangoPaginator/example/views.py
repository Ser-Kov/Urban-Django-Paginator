from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_page(request):
    title = 'Посты'
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj
    }
    return render(request, 'post_page.html', context)
