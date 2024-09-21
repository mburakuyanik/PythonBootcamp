from django.shortcuts import render, redirect
from . import models


# Create your views here.

def list_tweet(request):
    all_tweets = models.Tweets.objects.all()
    tweets_dict = {'all_tweets': all_tweets }
    return render(request, "tweetapp/list_tweet.html",context=tweets_dict)

def add_tweet(request):
    if request.method == "POST":
        nickname = request.POST["nickname"]
        tweeted = request.POST["tweeted"]
        models.Tweets.objects.create(nickname=nickname, tweet=tweeted)
        return redirect("tweetapp:list_tweet")
    else:
        return render(request, 'tweetapp/add_tweet.html',context={})
