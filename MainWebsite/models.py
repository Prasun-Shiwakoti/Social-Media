
from django.db import models
import json

def defaultJsonValue():
    return '[]'
def defaultChatValue():
    return '{}'

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    PublisherUsername = models.CharField(max_length=100, default=" ")
    Publisher = models.CharField(max_length=100, default=" ")
    PublisherImage = models.ImageField(upload_to="PostImages",blank=True)
    PublishDate = models.DateField(auto_now_add=True, blank=True)
    Content = models.TextField(default=" ", blank=True)
    Image = models.ImageField(upload_to="PostImages",blank=True)
    Comments = models.JSONField(default=defaultJsonValue)
    Likers = models.JSONField(default=defaultChatValue)

    @property
    def getComments(self):
        comments = json.loads(self.Comments)
        for comment in comments:
            comment["commenter"] = json.loads(comment["commenter"])[0]["fields"]
        return comments
    
    @property
    def getLikers(self):
        return json.loads(self.Likers)

    @property
    def totalComments(self):
        return len(json.loads(self.Comments))

    @property
    def totalLikes(self):
        return len(json.loads(self.Likers))

    def __str__(self) -> str:
        return self.Content

class DetailedUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, default=" ")
    gender = models.CharField(max_length=10, default="male")
    status = models.CharField(max_length=10, default="online")
    friends = models.JSONField(default=defaultJsonValue)
    image = models.ImageField(upload_to="UserProfilePics", default="/UserProfilePics/default.jpg")
    fname = models.CharField(max_length=100, default=" ", blank=True)
    lname = models.CharField(max_length=100, default=" ", blank=True)
    chats = models.JSONField(default=defaultChatValue)
    # followers = 1000

    def __str__(self):
        return self.username

    def followers(self):
        return len(json.loads(self.friends))