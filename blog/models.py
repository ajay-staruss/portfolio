from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 30000)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length = 40000)
    blog_image = models.ImageField(upload_to='images/')

def summary(self):
    return self.body[:125]
def __str__(self):
    return self.title
