from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()

	def __str__(self):
	    return self.title

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')