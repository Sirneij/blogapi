from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 2000)
    slug = models.SlugField(max_length=4000)
    subtitle = models.CharField(max_length = 2000, blank=True, null=True)
    image   = models.ImageField(upload_to='posts_pics', default='logo.svg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
