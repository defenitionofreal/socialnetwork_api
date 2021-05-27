from django.db import models
from users.models import User
from django.utils.text import slugify

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def likes_count(self):
        return self.likes


class Like(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} liked by {self.liker.author}"


