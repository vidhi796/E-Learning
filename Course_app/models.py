from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Card_list(models.Model):
    cad_id =models.AutoField(primary_key=True)
    User =models.ForeignKey(User, on_delete=models.CASCADE,null=False) 
    title = models.CharField(max_length=200)  # Title of the card
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)  # Optional image for card
    
    def __str__(self):
        return self.title


class Topic(models.Model):
    top_id =models.AutoField(primary_key=True)
    Chapter_title= models.CharField(max_length=200)  
    card_list = models.ForeignKey(Card_list, related_name='topics', on_delete=models.CASCADE)  # Foreignkey to Card
    title1= models.CharField(max_length=200)
    title2= models.CharField(max_length=200)
    title3= models.CharField(max_length=200)
    title4= models.CharField(max_length=200)
    title5= models.CharField(max_length=200)
    title6= models.CharField(max_length=200)

    
    def __str__(self):
        return self.top_id 


class TopicDetail(models.Model):
    top_detail_id =models.AutoField(primary_key=True)
    topic = models.OneToOneField(Topic, related_name='detail', on_delete=models.CASCADE)  # One-to-One relationship with Topic
    content = models.TextField() 
    image = models.ImageField(upload_to='card_images/', blank=True, null=True) 
    t1 =models.CharField(max_length=50)
    content_t1 = models.TextField()
    code_t1 = models.TextField()
    t2 =models.CharField(max_length=50)
    content_t2 = models.TextField()
    code_t2 = models.TextField()
    t3 =models.CharField(max_length=50)
    content_t3 = models.TextField()
    code_t3 = models.TextField()
    t4 =models.CharField(max_length=50)
    content_t4 = models.TextField()
    code_t4 = models.TextField()
    
    def __str__(self):
        return f"Detail of {self.topic.title}"
 
