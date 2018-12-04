from django.db import models

# Create your models here.


class Article(models.Model):
    post_title = models.CharField(max_length=100 , null=True) #title of the thread under crawl,
    post_id = models.IntegerField(unique=True,null=True)    #unique identifier of the concerned post.To be scraped form the site,
    post_url = models.CharField(max_length=100)   #url of the post under crawl,
    publish_time = models.DateTimeField()         #time when the post was published,
    fetch_time = models.DateTimeField()           #time when the post was fetched,
    author = models.CharField(max_length=50, null=True)      #author of the post
    post_text = models.TextField(null=True) #text content of the post



