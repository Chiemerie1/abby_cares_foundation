from django.db import models
from tinymce import models as tinymce_models

# Create your models here.


class MainHeroSectionImage(models.Model):
    image = models.ImageField(
        blank=False,
        upload_to="main_hero_image"
    )

    def __str__(self):
        return "main image"
     


class NewsAndUpdate(models.Model):

    # class NewsAndUpdateManager(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset()[:10]
        
    image = models.ImageField(
        blank=False,
        upload_to="homepage_what_we_have_done"
    )
    Headline = models.CharField(max_length=30)
    paragraph = tinymce_models.HTMLField()

    def snip(self):
        return self.paragraph[:50] + "..."
    
    def __str__(self):
        return self.Headline
    


class NewMajorOutreach(models.Model):
    # class NewMajorOutreachManager(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().last()
  
    title = models.CharField(max_length=30)
    top_image = models.ImageField(
        blank=False,
        upload_to="major_outreach"
    )
    right_image = models.ImageField(
        blank=False,
        upload_to="major_outreach"
    )
    left_image = models.ImageField(
        blank=False,
        upload_to="major_outreach"
    )
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
    def snip(self):
        return self.paragraph[:50] + "..."
    


class Blog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(
        blank=False,
        upload_to="major_outreach"
    )
    paragraph = tinymce_models.HTMLField()
    writers_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def snip(self):
        return self.paragraph[:50] + "..."
    
    def __str__(self):
        return self.title
    
