from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post, Category


class PostListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        # Only show published posts
        return Post.objects.filter(
            published=True,
            published_date__lte=timezone.now()
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        # Base queryset (show unpublished in preview mode)
        if self.request.GET.get('preview'):
            return Post.objects.all()
        # Regular view - only published posts
        return Post.objects.filter(
            published=True, 
            published_date__lte=timezone.now()
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        # Get related posts (same category)
        related = Post.objects.filter(
            published=True,
            published_date__lte=timezone.now(),
            categories__in=post.categories.all()
        ).exclude(id=post.id).distinct()[:3]
        
        context['related_posts'] = related
        return context


class CategoryPostsView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(
            categories=self.category,
            published=True,
            published_date__lte=timezone.now()
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context