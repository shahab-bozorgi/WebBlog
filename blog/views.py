from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog.models import Post, Category, Comment, Message, Like
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessagesForm
from django.views.generic import View, ListView, DetailView
from django.views.generic.base import TemplateView, RedirectView
from .mixins import LoginRequiredMixin


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, post=post, user=request.user, parent_id=parent_id)

    return render(request, 'blog/post_details.html', {'post': post})


def post_list(request):
    posts = Post.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(posts, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/posts_list.html', {'posts': object_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    posts = category.posts.all()
    return render(request, 'blog/posts_list.html', {'posts': posts})


def search(request):
    q = request.GET.get('q')
    posts = Post.objects.filter(title__contains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(posts, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/posts_list.html', {'posts': object_list})


def contact_us(request):
    if request.method == 'POST':
        form = MessagesForm(data=request.POST)
        pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

    else:
        form = MessagesForm()
    return render(request, 'blog/contact_us.html', {'form': form})


class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 1
    queryset = Post.objects.all()
    template_name = 'blog/posts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'mohammd'
        return context

class PostDetailView( DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(post__slug=self.object.slug, user_id=self.request.user.id):
            context["is_liked"] = True
        else:
            context["is_liked"] = False
        return context


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(post__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({'response': 'unliked'})


        except:
            Like.objects.create(post_id=pk, user_id=request.user.id)
            return JsonResponse({'response': 'liked'})

