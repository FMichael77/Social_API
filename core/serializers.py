from rest_framework import serializers
from .models import Profile, Post, Comment

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
                'pk',
                'name',
                'email',
                'street',
                'suite',
                'city',
                'zipcode'
            )

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'body'
        )

class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(read_only = True, many = True)

    class Meta:
        model = Profile
        fields = (
                'pk',
                'name',
                'posts'
            )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = (
                'pk',
                'name',
                'body'
            )

class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(read_only = True, many = True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'title',
            'body',
            'comments'
        )