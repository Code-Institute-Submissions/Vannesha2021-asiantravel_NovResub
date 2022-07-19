from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPost.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('post_like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('edit_post/<slug:slug>', views.EditPostView.as_view(), name='edit_post'),
    path('delete_post/<slug:slug>', views.DeletePostView.as_view(), name='delete_post'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
]