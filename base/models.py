from django.db import models
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 200)
    descrption = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(null=True, unique=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("update", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        

    class Meta:
        ordering = ['complete']


