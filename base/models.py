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

class PDPR(models.Model):
    NEVER = '1'
    OCCASIONALLY = '2'
    SOMETIMES = '3' 
    OFTEN = '4' 
    ALWAYS = '5' 

    PDPR_CHOICES = [
        (NEVER, 'Never'), 
        (OCCASIONALLY, 'Occasionally'),
        (SOMETIMES, 'Sometimes'),
        (OFTEN, 'Often'),
        (ALWAYS, 'Always')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    q1 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q2 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q3 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q4 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q5 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q6 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q7 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q8 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q9 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q10 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q11 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q12 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q1 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q13 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q14 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )
    q15 = models.CharField(
        max_length=1,
        choices=PDPR_CHOICES,
        default=NEVER
    )

    def __str__(self):
        return str(self.user + '--' + str(self.date))



