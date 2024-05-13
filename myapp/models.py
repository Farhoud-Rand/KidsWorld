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
        ('2-5', '2-5'),
        ('6-9', '6-9'),
        ('10-12', '10-12')
    ] 
    LANGUAGE = [
        ('English', 'English'),
        ('Arabic','Arabic')
    ]         
    title = models.CharField(max_length= 255)
    genre = models.CharField(choices=CATEGORIES, max_length= 255, default='Adventure')
    language = models.CharField(choices=LANGUAGE, max_length= 255, default='English')
    age_limit = models.CharField(choices= AGE_LIMIT, max_length= 255)
    file = models.FileField(upload_to="PDFs/", null=True) #for tesing "we must back later"
    image = models.ImageField(upload_to="Images/", null=True)
    rate = models.PositiveBigIntegerField(default=0)
    users_who_like = models.ManyToManyField(User, related_name="favorite_stories")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__ (self):
        return f"{self.title}"
    
    #this function to serialize stories data
    @classmethod
    def serialize_stories(cls, stories):
        serialized_stories = [{
            'title': story.title,
            'genre': story.genre,
            'language': story.language,
            'age_limit': story.age_limit,
            'file_url': story.file.url if story.file else None,
            'image_url': story.image.url if story.image else None,
            'rate': story.rate,
            'created_at': story.created_at.isoformat(),
            'updated_at': story.updated_at.isoformat(),
            'users_who_like': [user.username for user in story.users_who_like.all()]
        } for story in stories]
        return serialized_stories
    
    # Get the newest 3 stories 
    @staticmethod
    def get_last_three():
        return Story.objects.order_by('-created_at')[:3]
    
    # Get all stories from database
    @staticmethod
    def get_all_stories():
        return Story.objects.all()
    
    # To get a specific story by using story
    @staticmethod
    def get_story_by_id(id):
        return Story.objects.get(id = id)


class Comment(models.Model):
    comment_content = models.TextField(null=True)
    user_who_comment = models.ForeignKey(User, related_name="user_who_comment", on_delete= models.CASCADE, null=True )
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments', null=True)
    created_at = models.DateTimeField(auto_now_add= True)

    # Add comment
    @staticmethod 
    def add_comment(request_data, user_id):
        story_id = request_data['id']
        user = get_user_by_id(user_id)
        story = Story.get_story_by_id(story_id)
        text = request_data['comment']
        Comment.objects.create(user=user, story=story, text=text)

class Rate(models.Model):
    user_who_rate = models.ForeignKey(User, related_name= "rate", on_delete= models.CASCADE)
    story_which_rate = models.ForeignKey(Story, related_name="story_rate", on_delete= models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

# To get a specific user by using user id
def get_user_by_id(id):
    return User.objects.get(id = id)