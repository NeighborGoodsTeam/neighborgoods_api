from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Business(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=1000, null=True)
  addressOne = models.CharField(max_length=100)
  addressTwo = models.CharField(max_length=100, null=True)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipCode = models.IntegerField(default=0)
  longitude = models.FloatField(default=0.0)
  latitude = models.FloatField(default=0.0)
  industry = models.CharField(max_length=100, null=True)
  phone = models.CharField(max_length=20, default=0)
  website = models.URLField(max_length=200, null=True)
  email = models.EmailField(max_length=100)
  logo = models.TextField(max_length=1000, null=True)
  # # hours =
  inventory = models.TextField(max_length=2000, null=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The business named {self.name}"

  def as_dict(self):
    """Returns dictionary version of Business models"""
    return {
        'id': self.id,
        'name': self.name,
    }

  # def user_directory_path(instance, filename):
  #   # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
  #   return 'user_{0}/{1}'.format(instance.user.id, filename)
