from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from pilkit.processors.resize import ResizeToFill
class User(AbstractUser):
    email = models.EmailField(max_length=50)

class Gallery(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='galleries')
    title = models.CharField(max_length = 250)
    date_created = models.DateField(auto_now=True)
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} {self.date_created}'

class Photo(models.Model):
    gallery = models.ForeignKey(to=Gallery, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length = 250)
    description = models.TextField(blank=True)
    alt_text = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/gallery_images/', null=True, blank=True)
    image_medium = ImageSpecField(
        source="image",
        processors=[ResizeToFit(500, 800, upscale=False)],
        format="JPEG",
        options={'quality': 75})
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 75})

    date_created = models.DateField(auto_now=True)
    default = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.gallery} {self.title} {self.description} {self.date_created}'


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=255)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.photo} {self.text} {self.date_created}'


