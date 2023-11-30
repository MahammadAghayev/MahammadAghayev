from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about')


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Haqqimizda'
        verbose_name_plural = 'Haqqimizda'

class AboutPoint(models.Model):
    about = models.ForeignKey(
        'about.About',
        on_delete = models.CASCADE,
        related_name = 'points',
    )
    text = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'Haqqimizda punktu'
        verbose_name_plural = 'Haqqimizda punktlari'
