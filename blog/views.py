from django.shortcuts import render
from .models import Blog
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


def blog_lists(request):
    blogs = Blog.objects.all()
    # pagination
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': blogs,
        'page_obj': page_obj
    }

    return render(request, 'blog/blog.html', context)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    similar_blog = blog.tags.similar_objects()[:4]
    comments = blog.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.save()

            messages.success(request, 'Your comment submitted.')
            return HttpResponseRedirect(request.path_info)

    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'similar_blog': similar_blog,
        'comments': comments
    }
    return render(request, 'blog/details.html', context)


def search_blog(request):
    queryset = Blog.objects.all()
    query = request.GET.get('q')

    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query) | Q(
                description__icontains=query)

        ).distinct()

    context = {
        'queryset': queryset,
        'query': query
    }
    return render(request, 'blog/search.html', context)
