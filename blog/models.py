from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost (models.Model):

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Post")
    slug = models.CharField(max_length=130, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    spotlight_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)

class Meta:
    ordering = ['-published_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=60)
    email = models.EmailField()
    published_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    body = models.TextField()

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

