from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    PDquote = models.BooleanField(default=False)

    def __str__(self):
        return str(self.author + ' -- ' + self.quote + ' -- ' + 'PD Quote: ' + str(self.PDquote))

class Image(models.Model):
  image = models.FileField()
  alt_text = models.TextField() 

  def __str__(self):
    return str(self.alt_text)