from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def showblog (request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})

def specific_post(request, post_id):   # post_id — конкретный пост из базы данных
    post = get_object_or_404(Post, pk=post_id)   # Еслистраница не найдена, будет 404. pk — Primary Key из базы данных
    return render(request, 'blog/specific_post.html', {'post': post})