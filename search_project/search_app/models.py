from django.db import models

from django.db import models 
 
class Category(models.Model): 
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name 
 
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, default="Unknown Title")
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, default="アルバム情報がありません")
    view_count = models.PositiveIntegerField(default=0)
    youtube = models.URLField(blank=True)
    apple_music = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=10)
    image_url = models.URLField(default='https://thumb.ac-illust.com/73/7387030e5a5600726e5309496353969a_t.jpeg')
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"
