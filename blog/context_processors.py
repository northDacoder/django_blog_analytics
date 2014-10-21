from blog.models import Post, Tag


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }



def tag_objects(request, tag):
    return {
        'tag_objects': Tag.posts_set.filter(tags_name=tag)
    }