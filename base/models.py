from django.db import models
from members.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    PDquote = models.BooleanField(default=False)

    def __str__(self):
        return str(self.author + ' -- ' + self.quote + ' -- ' + 'PD Quote: ' + str(self.PDquote))

class Image(models.Model):
  image = models.ImageField()
  alt_text = models.TextField() 

  def __str__(self):
    return str(self.alt_text)


class Reflection(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  date = models.DateField(auto_now_add=True)
  text = models.TextField() 

  def __str__(self):
    return str(str(self.date) + ' -- ' + self.text)