from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
#zapisywanie do bazy danych
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## if user is deleted remove his posts
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)
    