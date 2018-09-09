from django.db import models

# Create your models here.
from django.urls import reverse

from django.contrib.auth.decorators import login_required

def upload_location(instance,filename):
    return '%s/%s'%(instance.id,filename)


class Post(models.Model):
    # user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
    issue=models.CharField(max_length=500)
    image=models.ImageField(upload_to='upload_location',
        null=True,blank=True,width_field="widthfield",height_field="heightfield")
    widthfield=models.IntegerField(default=10)
    heightfield=models.IntegerField(default=10)
    complaint=models.TextField()
    location=models.CharField(max_length=100)
    update=models.DateTimeField(auto_now=True,auto_now_add=False)
    time=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse("detail",kwargs={'id':self.id})

    class Meta:
        ordering=["-time","-update"]