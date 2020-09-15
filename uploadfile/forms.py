from django import forms 
from .models import track, FileTypes, NumberofStems, ContactModel

class TrackForm(forms.ModelForm):

	class Meta:
		model = track

		fields = ['YTLink', 'audio', 'OutputType', 'NStems']

		widgets = {
			'audio': forms.FileInput(attrs={'accept': 'audio/*', 'placeholder':'Choose an audio file...'}),
			'OutputType': forms.Select(choices = FileTypes),
			'NStems': forms.Select(choices = NumberofStems),
			'YTLink': forms.TextInput(attrs={'placeholder': 'Enter Youtube link...'})
		}

		labels = {
			'OutputType' : "Format",
			'NStems': "Output Type",
			'audio' : "Upload Audio File:",
			'YTLink': "Youtube Link:"
		}

	def clean(self):
		cleaned_data = super(TrackForm, self).clean()

		audio = cleaned_data.get("audio")
		YTLink = cleaned_data.get("YTLink")

		if audio and YTLink:
			raise forms.ValidationError("Submit only one of Youtube link or Audio file")
		elif not audio and not YTLink:
			raise forms.ValidationError("Submit either Youtube link or Audio file")

		return cleaned_data


class ContactForm(forms.ModelForm):

	class Meta:
		model = ContactModel

		fields = ['FromEmail', 'Subject', 'Message']

		widgets = {
			'FromEmail': forms.TextInput(attrs={'placeholder': 'Enter your email id:'}),
			'Subject': forms.TextInput(attrs={'placeholder': 'Enter subject...'}),
			'Message': forms.Textarea(attrs={'placeholder': 'Enter message...', 'rows':5})
		}

		labels = {
			'FromEmail': 'Email ID:',
			'Subject': 'Subject(Optional):',
			'Message': 'Message:'
		}

