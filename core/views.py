from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Skills
from .forms import ContactForm
from projects.models import Project


class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get featured projects (limit to 3)
        context['featured_projects'] = Project.objects.filter(
            is_featured=True
        ).order_by('-date_completed')[:5]
        
        # Get skills grouped by category
        skills = Skills.objects.all()
        skills_by_category = {}
        for skill in skills:
            category_display = skill.get_category_display()
            if category_display not in skills_by_category:
                skills_by_category[category_display] = []
            skills_by_category[category_display].append(skill)
        
        context['skills_by_category'] = skills_by_category
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skills.objects.all()
        return context


class ContactView(CreateView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 
            "Thank you for your message! I'll get back to you soon."
        )
        return response
