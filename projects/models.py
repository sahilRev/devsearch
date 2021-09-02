from django.db import models
import uuid
from users.models import Profile
# Create your models here.



class Project(models.Model):
    '''This is the "project" Entity'''    
    
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=200 , null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag' , blank=True)
    vote_total = models.IntegerField(default=0 , null=True , blank= True)
    vote_ratio = models.IntegerField(default=0 , null=True , blank= True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False)

    def __str__(self):
        return self.title



class Review(models.Model):
    '''This is the "Review" Entity -> Each project will have a review'''    

    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down' , 'Down Vote'),
    )
    # owner = 
    project = models.ForeignKey( Project , on_delete=models.CASCADE )          #models.CASCADE deletes all reviews is corresponding project is deleted
    body = models.TextField(null=True , blank=True)
    value = models.CharField(max_length=200 , choices=VOTE_TYPE )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False)

    def __str__(self):
        return self.value



class Tag(models.Model):
    '''Tags for the project like (ReactJS, Python)'''

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False)

    def __str__(self):
        return self.name