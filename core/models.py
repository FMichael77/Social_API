from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    street = models.CharField(max_length=80)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    user = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)