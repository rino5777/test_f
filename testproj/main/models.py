from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from user.models import Profile
# Create your models here.
class Skill(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    tag_skill = models.CharField(max_length=50, db_index=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager() 


    def __str__(self):
            return str(self.tag_skill)


    def get_absolute_url(self):
        return reverse('user:account', args=[self.tag_skill])

class Value_skill(models.Model):
    to_tag_skill = models.ForeignKey(Skill, related_name='tag', on_delete=models.CASCADE)
    value  = models.CharField(max_length=100, db_index=True, unique=True)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)

    def __str__(self):
            return str(self.value)



class Skills(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return str(self.name)