from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField
import datetime



class Post(models.Model):
    title 		= models.CharField(max_length=50,blank=False)
    image               = ThumbnailerImageField(upload_to='news_photos', blank=True)
    content 		= RichTextField()
    draft           	= models.BooleanField(default=False)
    publish         	= models.DateField(auto_now=False, auto_now_add=False,default=datetime.date.today)
    viewcount       	= models.IntegerField(default=0)
    updated         	= models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp       	= models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return self.title
    def increase_views(self):
        self.viewcount  += 1
        self.save(update_fields=['viewcount'])
