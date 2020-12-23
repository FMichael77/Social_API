import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_api.settings')
django.setup()

from core.models import Profile, Post, Comment

def main():
    with open('db.json', 'r') as f:
        data = json.load(f)

    profiles = data['users']
    posts = data['posts']
    comments = data['comments']

    save_users(profiles)
    save_posts(posts)
    save_comments(comments)

def save_users(profiles):
    profile_list = []

    for profile in profiles:
        profile_list.append(
            Profile(
                id = profile['id'],
                name = profile['name'],
                email = profile['email'],
                street = profile['address']['street'],
                suite = profile['address']['suite'],
                city = profile['address']['city'],
                zipcode= profile['address']['zipcode']
            )
        )

    Profile.objects.bulk_create(profile_list)

def save_posts(posts):
    posts_list = []

    for post in posts:
        posts_list.append(
            Post(
                user = Profile.objects.get(id=post['userId']),
                id = post['id'],
                title = post['title'],
                body = post['body']
            )
        )

    Post.objects.bulk_create(posts_list)

def save_comments(comments):
    comments_list = []

    for comment in comments:
        comments_list.append(
            Comment(
                post = Post.objects.get(id=comment['postId']),
                id = comment['id'],
                name = comment['name'],
                email = comment['email'],
                body = comment['body']
            )
        )

    Comment.objects.bulk_create(comments_list)

main()
