from django.contrib import admin
from .models import Category, Project, Technology


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class TechnologyInline(admin.TabularInline):
    model = Project.technologies.through
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed', 'is_featured')
    list_filter = ('is_featured', 'categories')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TechnologyInline]
    filter_horizontal = ('categories',)
    exclude = ('technologies',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')