from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    # null=True means that we dont have to set the description.
    # blank=True means that we will be able to submit this form with the description value being empty.
    description = models.TextField(null=True, blank=True) 
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField("Tag",blank=True)
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)

    # auto_now_add=True will add the date&time (timestamp) value to the "created" whenever this model will be created.
    created = models.DateTimeField(auto_now_add=True)
    # default=uuid.uuid4: Automatically generates a unique UUID for each new instance
    # unique=True: Ensures that no two instances have the same UUID
    # primary_key=True: Uses this field as the primary key instead of the default auto-incrementing integer
    # editable=False: Prevents the UUID from being edited in forms or the admin interface
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE = (
        ("up","Up Vote"),
        ("down","Down Vote"),
    )
    # owner =
    # "on_delete=models.SET_NULL means that if a project will get deleted the review will be left but as a null value
    # "on_delete=models.CASCADE means that if a project will get deleted the review will also be deleted
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 
    
    def __str__(self):
        return self.value
       
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    