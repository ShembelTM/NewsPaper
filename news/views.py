from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory
from datetime import datetime
from .filters import PostFilter



class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class NewsFilter(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'search_news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = PostFilter(self.request.GET, queryset)

        for post in self.filterset.qs:
            post.text_categories = ', '.join(
                list(PostCategory.objects.filter(post=post).values_list('category__category', flat=True))
            )

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostsDetail(DetailView):
    model = Post
    template_name = 'news1.html'
    context_object_name = 'news1'