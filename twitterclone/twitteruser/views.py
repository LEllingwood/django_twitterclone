from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from twitterclone.twitteruser.forms import SignupForm


# homepage render - user's homepage
@login_required
def homepage(request):
    html = "homepage.html"
    tweet = Tweet.order_by(Tweet.tweet_time)
    list_of_tweets = tweet.objects.filter(
        following=True) | Tweet.objects.filter(request.user.twitteruser)
    return render(request, html, {'data': list_of_tweets})
    # list_of_tweets is meant to filter the tweets to collect the tweets of the people user is following, as well as user.


# profile view - user's profile page
def profile_view(request, username):
    # username in ln 22 is a slug
    html = 'profile.html'

    username = TwitterUser.objects.filter(id=id)
    user_tweets = Tweet.objects.filter(username=username)
    # tweet_count=
    # followers =
    return render(request, html, {'data': username, 'tweets': user_tweets})

# for each user, including yourself - for all profile detail views
# how many people they're following
# their tweets
# their handle/username
# count of tweets

# tweet object needs two buttons - one that goes to the profile of the person who wrote the tweet and the date of the tweet

# tweet view is just the singletweet
# you can also click on the @name to get to their profile.

# check into .count() to increment the tweets


def signup_view(request):
    html = "generic_form.html"
    form = None

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'], password=data['password'])
            login(request, user)
            TwitterUser.objects.create(
                handle=data['handle'],
                user=user
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignupForm()
    return render(request, html, {'form': form})


# logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
