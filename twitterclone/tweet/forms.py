# import datetime
from django.utils import timezone
from django import forms

# form is what you're going to present to the end user


class TweetAddForm(forms.Form):
    tweet_text = forms.CharField(max_length=140)
    tweet_time = timezone.now()