from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

Result = (
    ('W', 'Win'),
    ('T', 'Tie'),
    ('L', 'Loss')
)

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    players = models.CharField(max_length=100)
    playtime = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
    def played_recently(self):
        return self.record_set.filter(date=date.today()).count() >= len(Result)

class Record(models.Model):
    date = models.DateField('Date Played')
    result = models.CharField(
        max_length=1,
        choices = Result,
        default = Result[0][0]
        )
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE) #this is so that when a game is deleted, it deletes related result too

    def __str__(self):
        return f"{self.get_result_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']