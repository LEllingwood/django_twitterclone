from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from twitterclone.tweet.models import Tweet
from twitterclone.tweet.forms import TweetAddForm


def tweet(request, id):
    html = "homepage.html"
    tweet = Tweet.objects.filter(id=id)
    return render(request, html, {'data': tweet})


@login_required()
def tweet_add(request):
    html = 'tweet_add.html'
    form = None

    if request.method == 'POST':
        form = TweetAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_tweet = Tweet.objects.create(
                username=request.user.twitteruser,
                tweet_text=data['tweet_text']
            )
            return render(request, 'tweet_add.html', {'new_tweet': new_tweet})

    else:
        form = TweetAddForm()
    return render(request, html, {'form': form})
    # TODO ADD conditional statement that if the tweet has an @, that user receives a notification.