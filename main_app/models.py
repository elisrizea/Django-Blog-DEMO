from django.db import models

# Create your models here.
class Posts(models.Model):
    post_author=models.CharField(max_length=150, null=False)
    title = models.CharField(max_length=150, null=False)
    content=models.TextField(null=False)
    date=models.DateTimeField(null=False,auto_now_add=True)

