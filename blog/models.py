from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    draft =  models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    comment = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    create_at = models.DateTimeField(default= timezone.now())

    def __str__(self) -> str:
        return self.comment