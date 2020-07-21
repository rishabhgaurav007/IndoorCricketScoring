from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    runs = models.IntegerField(default=0)
    fifties = models.IntegerField(default=0)
    hundreds = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    matches = models.IntegerField(default=0)
    notouts = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name+" "+self.last_name

    def average(self):
        if self.matches==0:
            return 0
        if self.matches-self.notouts<=0:
            return self.runs
        return round(self.runs/(self.matches-self.notouts),2)

class Score(models.Model):
    runscored = models.IntegerField(default=0)
    scoredby = models.IntegerField(default=0)
    wicketby = models.IntegerField(default=0)
    nameofbatsmen = models.CharField(max_length=30)
    nameofbowler = models.CharField(max_length=30)

    def __str__(self):
        return str(self.runscored)+" "+self.nameofbatsmen+" "+self.nameofbowler
