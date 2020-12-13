from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    cover_img = models.ImageField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    preview_text = models.CharField(max_length=200)
    project_url = models.CharField(max_length=200)
    git_repo = models.CharField(max_length=200, default=False)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title