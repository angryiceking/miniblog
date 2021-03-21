from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    BLOG_TYPE =( 
        ("TECH", "Technology"),
        ("GAME", "Games"),
        ("INTR", "Interests"),
        ("RAND", "Random Things"),
    )

    blog_title = models.CharField(max_length=255)
    blog_created_date = models.DateTimeField(auto_now_add=True)
    blog_content = RichTextField()
    blog_type = models.CharField(max_length=255, choices=BLOG_TYPE)

    def __str__(self):
        return self.blog_title