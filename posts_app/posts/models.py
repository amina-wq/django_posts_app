from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Posts(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_time = models.DateTimeField('date published', default=timezone.now)
    description = models.TextField('description')
    is_moderate = models.BooleanField('is moderated', default=False)

    class Meta:
        app_label = 'posts'
        ordering = ('-date_time', 'title')
        verbose_name = 'Publication'
        verbose_name_plural = 'Publication'

    def __str__(self):
        if self.is_moderate:
            status = 'OK'
        else:
            status = 'IN PROGRESS'
        return f'{status} {self.title} {self.date_time}'


class PostComments(models.Model):
    post_id = models.IntegerField('comments to the post')
    author = models.CharField(max_length=200)
    text = models.TextField('comment')
    date_time = models.DateTimeField('date published', default=timezone.now)

    class Meta:
        app_label = 'posts'
        ordering = ('-date_time', 'post_id')
        verbose_name = 'Post comment'
        verbose_name_plural = 'Post comments'

    def __str__(self):
        return f'{self.post_id} {self.date_time} {self.author}'


class PostRatings(models.Model):

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        to=Posts,
        on_delete=models.CASCADE
    )
    status = models.BooleanField(default='False')

    class Meta:
        app_label = 'posts'
        ordering = ('-post', 'author')
        verbose_name = 'Post rating'
        verbose_name_plural = 'Posts ratings'

    def __str__(self):
        if self.status:
            like = 'LIKE'
        else:
            like = 'DISLIKE'
        return f'{self.post.title} {self.author.username} {like}'


class Complaints(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField(default=timezone.now())

    class Meta:
        app_label = "posts"
        ordering = ("-date_time", "title")
        verbose_name = "Create complaint"
        verbose_name_plural = "Create complaints"

    def __str__(self):
        return f'{self.title} {self.description} {self.date_time}'