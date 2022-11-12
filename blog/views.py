from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import BlogPost as BlogPostModel
from .models import Profile as ProfileModel
from .forms import CommentForm, BlogForm, ProfileForm
from django.utils.text import slugify


class BlogPost(generic.ListView):
    model = BlogPostModel
    template_name = "index.html"
    paginate_by = 6
    fields = '__all__'
    
    def get_queryset(self):
        # user = self.request.user
        # if user.is_anonymous:
        return BlogPostModel.objects.filter(status=1).order_by('-published_on')
        # else:
        #     return BlogPostModel.objects.filter(status=1, author=user).order_by('-published_on')


class PostDetail(View):
    def get (self, request, slug, *args, **kwargs):
        queryset = BlogPostModel.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-published_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post (self, request, slug, *args, **kwargs):
        queryset = BlogPostModel.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-published_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment will be verified and published soon')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class PostLike(View):
    def post (self, request, slug):
        post = get_object_or_404(BlogPostModel, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(generic.CreateView):

    model = BlogPostModel
    template_name = 'add_post.html'
    fields = ['title', 'content', 'excerpt', 'status']
    success_url = '/'

    def form_valid(self, form): 
        """ adding the username automatically for the post """
        form.instance.author = self.request.user 
        return super().form_valid(form)


class EditPostView(View):

    model = BlogPostModel
    template_name = 'edit_post.html'
    fields = ['title', 'content', 'excerpt', 'status', 'spotlight_image']
    success_url = '/'

    def post (self, request, slug, *args, **kwargs):
        print(request.POST)
        blog = BlogPostModel.objects.get(slug=slug)
        new_title = request.POST["title"]
        new_content = request.POST["content"]
        new_excerpt = request.POST["excerpt"]
        new_status = request.POST["status"]
        blog.content=new_content
        blog.title = new_title
        blog.excerpt = new_excerpt
        blog.status = new_status
        blog.save()
        messages.success(request, 'Your post has been edited succesfully')
        return HttpResponseRedirect(reverse('edit_post', args=[slug]))

    def get(self, request, slug, *args, **kwargs):
        blogpost = BlogPostModel.objects.get(slug=slug)
        form = BlogForm(instance=blogpost)

        return render(
            request,
            "edit_post.html", 
             {
                "form": form,
                "blog": slug
             }
        )


class DeletePostView(View):

    model = BlogPostModel
    template_name = 'delete_post.html'
    success_url = '/'

    def post(self, request, slug, *args, **kwargs):
        print(request.POST)
        blog = BlogPostModel.objects.get(slug=slug)
        
        blog.delete()
        return HttpResponseRedirect(reverse('home'))

    def get(self, request, slug, *args, **kwargs):
        blogpost = BlogPostModel.objects.get(slug=slug)
        form = BlogForm(instance=blogpost)

        return render(
            request,
            "delete_post.html", 
             {
                "blog": slug
             }
        )


class Profile (View):
    model = ProfileModel
    template_name = 'profile.html'
    success_url = '/'

    def get (self, request):
        user=self.request.user
        context = {"user": user}
        try:
            ProfileModel.objects.get(user=user)
        except:
            ProfileModel.objects.create(user=user)
        return render (request, 'profile.html', context)

    def post (self, request, user, *args, **kwargs):
        print(request.POST)
        profile = Profile.objects.get(user=user)
        new_bio = request.POST["bio"]
        new_facebook = request.POST["facebook"]
        new_instagram = request.POST["instagram"]
        new_linkedin = request.POST["linkedin"]
        profile.bio = new_bio
        profile.facebook = new_facebook
        profile.instagram = new_instagram
        profile.linkedin = new_linkedin
        profile.save()
        return HttpResponseRedirect(reverse('edit_profile', args=[user]))


class EditProfileView (View):
    model = ProfileModel
    template_name = 'edit_profile.html'
    success_url = 'edit_profile.html'
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        profile = ProfileModel.objects.get(user=user)
        form = ProfileForm (instance=profile)
        
        return render(
            request,
            "edit_profile.html", 
             {
                "form": form,
             }
        )


    def post (self, request, *args, **kwargs):
        print(request.POST)
        user = self.request.user
        profile = ProfileModel.objects.get(user=user)
        new_bio = request.POST["bio"]
        new_facebook = request.POST["facebook"]
        new_instagram = request.POST["instagram"]
        new_linkedin = request.POST["linkedin"]
        profile.bio = new_bio
        profile.facebook = new_facebook
        profile.instagram = new_instagram
        profile.linkedin = new_linkedin
        profile.save()
        messages.success(request, 'Your profile has been edited succesfully')
        return HttpResponseRedirect(reverse('edit_profile'))

