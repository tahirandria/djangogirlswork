from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    Tahiry=Post.objects.all()
    return render(request, 'blog/post_list.html', {"Posts": Tahiry})
