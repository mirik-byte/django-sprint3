from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


POSTS_PER_PAGE = 5


def _get_published_posts():
    """Return base queryset of published posts."""
    now = timezone.now()
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=now,
        category__is_published=True
    )


def index(request):
    post_list = _get_published_posts()[:POSTS_PER_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        _get_published_posts(),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = _get_published_posts().filter(category=category)
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
