from django.urls import path
from . import views

app_name ="tweetapp"

urlpatterns = [
    path('list_tweet/',views.list_tweet, name='list_tweet' ), #burakuyanik/tweetapp/list_tweet
    path('add_tweet/',views.add_tweet,name='add_tweet')
]