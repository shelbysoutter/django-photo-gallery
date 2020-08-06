from django.db import models
from users.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

# Create your models here.

class Album(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    featured_photo = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name= '+',  null=True, blank=True)
    title = models.CharField(max_length = 50)
    public = models.BooleanField(default=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_album', blank=True)


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_photos', blank=True)
    photo = models.ImageField(upload_to='photo_photos/', null=True, blank=False)
    photo_thumbnail = ImageSpecField(
        source="photo",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )
    albums = models.ManyToManyField(Album, related_name='photos', blank=True)