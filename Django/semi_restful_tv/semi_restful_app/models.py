from django.db import models
import datetime


class ShowtimeManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        shows = Showtime.objects.all()
        today = datetime.datetime.now().strftime("%Y%m%d")
        show_date = postData['date'].replace("-", "")
        if len(postData['title']) < 2:
            errors["title"] = "Blog name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog description should be at least 3 characters"
        if len(postData['desc']) < 10 and len(postData['desc']) > 0:
            errors["desc"] = "Blog description should be at least 10 characters"
        if show_date > today:
            errors['date'] = "The release date must be in the past!"
        for titles in shows:
            if postData['title'] == titles.title:
                errors['title'] = "This title already exists!"
        return errors


class Showtime(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowtimeManager()
