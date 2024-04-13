from blog.models import Post, Category


def recent_posts(request):
    recent_posts = Post.objects.order_by('-created')[:3]
    categories = Category.objects.all()
    return {'recent_posts': recent_posts, 'categories':categories}