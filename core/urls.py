from django.urls import path
from core import views

urlpatterns = [
    path('', views.ApiRoot.as_view(),
         name=views.ApiRoot.name),
    path('profiles/', views.ProfileList.as_view(),
         name=views.ProfileList.name),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(),
         name=views.ProfileDetail.name),
    path('profiles-posts/', views.ProfilePostList.as_view(),
         name=views.ProfilePostList.name),
    path('profiles-posts/<int:pk>/', views.ProfilePostDetail.as_view(),
         name=views.ProfilePostList.name),
    path('posts-comments/', views.PostCommentList.as_view(),
         name=views.PostCommentList.name),
    path('posts-comments/<int:pk>/', views.PostCommentDetail.as_view(),
         name=views.PostCommentDetail.name),
    path('posts/<int:post>/comments/', views.CommentList.as_view(),
         name=views.CommentList.name),
    path('posts/<int:post>/comments/<int:pk>/', views.CommentDetail.as_view(),
         name=views.CommentDetail.name),
]
