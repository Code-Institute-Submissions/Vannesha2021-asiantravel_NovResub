from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=130, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="BlogPost"
    )
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)


