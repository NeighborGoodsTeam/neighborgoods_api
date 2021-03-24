from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Business(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=1000)
  addressOne = models.CharField(max_length=100)
  addressTwo = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipCode = models.IntegerField()
  longitude = models.FloatField()
  latitude = models.FloatField()
  industry = models.CharField(max_length=100)
  phone = models.IntegerField()
  website = models.URLField(max_length=200)
  email = models.EmailField(max_length=100)
  # hours =
  inventory = models.FileField(upload_to='user_directory_auth/')
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The business named '{self.name}' is {self.color} in color. It is {self.ripe} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Business models"""
    return {
        'id': self.id,
        'name': self.name,
        'ripe': self.ripe,
        'color': self.color
    }

  # def user_directory_path(instance, filename):
  #   # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
  #   return 'user_{0}/{1}'.format(instance.user.id, filename)
