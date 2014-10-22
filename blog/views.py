from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })

#
# def tag(request, tag_name):
#     tags = Post.objects.filter(tag=tag_name)
#     return render(request, 'blog.html', {"posts": tags})



# def posts_by_tag(request, tag_pk):
#