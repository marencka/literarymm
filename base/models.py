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
  image = models.ImageField(upload_to='images/')
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
    class Scores(models.IntegerChoices):
        NEVER = '1'
        OCCASIONALLY = '2'
        SOMETIMES = '3' 
        OFTEN = '4' 
        ALWAYS = '5' 

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    q1 = models.IntegerField(choices=Scores.choices)
    q2 = models.IntegerField(choices=Scores.choices)
    q3 = models.IntegerField(choices=Scores.choices)
    q4 = models.IntegerField(choices=Scores.choices)
    q5 = models.IntegerField(choices=Scores.choices)
    q6 = models.IntegerField(choices=Scores.choices)
    q7 = models.IntegerField(choices=Scores.choices)
    q8 = models.IntegerField(choices=Scores.choices)
    q9 = models.IntegerField(choices=Scores.choices)
    q10 = models.IntegerField(choices=Scores.choices)
    q11 = models.IntegerField(choices=Scores.choices)
    q12 = models.IntegerField(choices=Scores.choices)
    q1 = models.IntegerField(choices=Scores.choices)
    q13 = models.IntegerField(choices=Scores.choices)
    q14 = models.IntegerField(choices=Scores.choices)
    q15 = models.IntegerField(choices=Scores.choices)
    
    total = models.IntegerField(default = 0)
    def __str__(self):
        return str(str(self.user) + '--' + str(self.date))



