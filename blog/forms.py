from .models import Comment
from .models import Profile
from django import forms
from .models import BlogPost as BlogPostModel

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'facebook', 'instagram', 'linkedin' )


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ('title', 'content', 'excerpt', 'status')

