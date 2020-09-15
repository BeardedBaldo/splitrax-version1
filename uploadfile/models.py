from django.db import models

# Create your models here.
FileTypes = [
	('mp3', 'mp3'),
	('wav', 'wav'),
]

NumberofStems = [
	('2stems','2 stems - karaoke - vocals and instrumentals'),
	('4stems','4 stems - vocals, bass, drums and others'),
	('5stems','5 stems - vocals, bass, drums, piano and others'),
]

class track(models.Model):
	audio = models.FileField(null = True, blank= True, verbose_name = "")
	YTLink = models.URLField(null = True, blank = True, verbose_name = "")
	OutputType = models.CharField(max_length = 5, null = True)
	NStems = models.CharField(max_length = 10, null = True)
	DateTimeAdded = models.DateTimeField(null = True, auto_now = True)

	def save(self, *args, **kwargs):
		try:
			super(track, self).save(*args, **kwargs)
		except Exception as e:
			raise Exception ("Something went wrong" + e.message)


class ContactModel(models.Model):
	FromEmail = models.EmailField(null = True)
	Subject = models.CharField(blank = True, null = True, max_length = 50)
	Message = models.CharField(null = True, max_length = 1000)
	DateTimeAdded = models.DateTimeField(null = True, auto_now = True)


class FaqModel(models.Model):
	Question = models.CharField(null = True, max_length = 200)
	Answer = models.CharField(null = True, max_length = 2000)
	

class TermsModel(models.Model):
	Header = models.CharField(null = True, max_length = 50)
	Description = models.CharField(null = True, max_length = 2000)
