from django.db import models
from django.contrib.auth.models import User
class Story(models.Model):
    CATEGORIES = [
        ('Adventure', 'Adventure'),
        ('Animals', 'Animals'),
        ('Fantasy', 'Fantasy'),
        ('Science', 'Science')
    ]
    AGE_LIMIT = [
        ('2', '2'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('10', '10')
    ]          
    title = models.CharField(max_length= 255)
    genre = models.CharField(choices=CATEGORIES, max_length= 255)
    age_limit = models.CharField(choices= AGE_LIMIT, max_length= 255)
    file = models.FileField(upload_to="upload/") #for tesing "we must back later"
    users_who_like = models.ManyToManyField(User, related_name="favorite_stories")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
class Comment(models.Model):
    comment_content = models.CharField(max_length=255)
    user_who_comment = models.ForeignKey(User, related_name="user_who_comment", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
class Rate(models.Model):
    user_who_rate = models.ForeignKey(User, related_name= "rate", on_delete= models.CASCADE)
    story_which_rate = models.ForeignKey(Story, related_name="story_rate", on_delete= models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)