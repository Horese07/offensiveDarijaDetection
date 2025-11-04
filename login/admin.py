from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Comment

# Inline for comments
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ('author', 'content', 'approuvé', 'created_at')
    readonly_fields = ('created_at',)

# Article admin with image preview
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'image_tag')  # Add image preview column
    search_fields = ('title', 'content')
    list_filter = ('date_created',)
    inlines = [CommentInline]

    # Method to display image in list_display
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True

# Register models
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)  # Optional
