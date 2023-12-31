from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Meep(models.Model):
    user = models.ForeignKey(
        User, related_name="meeps",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="meep_like", blank=True)
    video = models.FileField(upload_to='meep_videos/', blank=True, null=True)  

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (
        f"{self.user} "
        f"({self.created_at:%Y-%m-%d %H:%M}): "
        f"{self.body}..."
    )

class Reply(models.Model):
    user = models.ForeignKey(User, related_name="replies", on_delete=models.CASCADE)
    meep = models.ForeignKey(Meep, related_name="replies", on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} ({self.created_at:%Y-%m-%d %H:%M}): {self.body}..."
        
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    
    date_modified= models.DateTimeField(User, auto_now=True)
    profile_image= models.ImageField(null=True, blank=True, upload_to="images/")
    
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    homepage_link= models.CharField(null=True, blank=True, max_length=500)
    facebook_link = models.CharField(null=True, blank=True, max_length=500)
    instagram_link = models.CharField(null=True, blank=True, max_length=500)
    linkedin_link = models.CharField(null=True, blank=True, max_length=500)
    def __str__(self):
        return self.user.username
     
     
     
     
@receiver(post_save, sender=User)  
def creat_profile(sender,instance, created, **kwargs):
    if created:
        user_profile= Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

