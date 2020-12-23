from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Profile, Post, Comment
from .serializers import ProfileSerializer, ProfilePostSerializer, PostCommentSerializer, CommentSerializer

class ProfileList(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profiles'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profile-detail'

class ProfilePostList(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfilePostSerializer
	name = 'profile-posts'

class ProfilePostDetail(generics.RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfilePostSerializer
	name = 'profile-posts-detail'

class PostCommentList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCommentSerializer
	name = 'posts-comments'

class PostCommentDetail(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCommentSerializer
	name = 'posts-comments-detail'

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name = 'comment-list'
	
	def get_queryset(self):
		queryset = Comment.objects.filter(post=self.kwargs.get('post'))
		return queryset
	
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name = 'comment-detail'

class ApiRoot(generics.GenericAPIView):
	name = 'api-root'

	def get(self, request,*args, **kwargs):
		return Response({
			'profile': reverse(ProfileList.name, request=request),
			'profile-posts': reverse(ProfilePostList.name, request=request), 
			'post-comments': reverse(PostCommentList.name, request=request),
		})