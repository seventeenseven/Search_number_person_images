
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.profile_image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_image.path)


class UploadImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploaded_images/', null=True)
    image_label = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class Comments(models.Model):
    image = models.ForeignKey(UploadImages, on_delete=models.CASCADE)
    comments = models.TextField()
    com_date = models.DateField(default=timezone.now)