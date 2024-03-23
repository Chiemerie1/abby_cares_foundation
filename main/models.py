from django.db import models

# Create your models here.


class NewsAndUpdate(models.Model):
    image = models.ImageField(
        blank=False,
        upload_to="homepage_what_we_have_done"
    )
    Headline = models.CharField(max_length=30)
    paragraph = models.TextField()

    def snip(self):
        return self.paragraph[:20] + "..."
    
    def __str__(self):
        return self.Headline
    
