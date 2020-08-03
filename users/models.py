from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
     def is_favorite_album(self, album):
        return self.favorite_album.filter(pk=album.pk).count() == 1

     def is_favorite_photo(self, photo):
        return self.favorite_photo.filter(pk=photo.pk).count() == 1