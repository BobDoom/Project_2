from django.db import models
# from datetime import datetime

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length = 70)            # Обязательно указывать  max_length
    post_date = models.DateTimeField() # (auto_now = True)
    post_text = models.TextField()                                 # Можно использовать для больших текстов, аргументы не важны
    post_image = models.ImageField(upload_to = 'post_images/')
    