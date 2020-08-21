from django.db import models

# Create your models here.
FileTypes = [
	('mp3', 'mp3'),
	('wav', 'wav'),
]

NumberofStems = [
	('2stems','2 stems'),
	('4stems','4 stems'),
	('5stems','5 stems'),
]

class track(models.Model):
	audio = models.FileField(null = True, blank= True)
	YTLink = models.URLField(null = True, blank = True)
	OutputType = models.CharField(max_length = 5, null = True)
	NStems = models.CharField(max_length = 10, null = True)