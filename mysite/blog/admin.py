from django.contrib import admin

from .models import BlogPost
from .models import BlogPostAdmin

# Register your models here.

admin.site.register(BlogPost, BlogPostAdmin)