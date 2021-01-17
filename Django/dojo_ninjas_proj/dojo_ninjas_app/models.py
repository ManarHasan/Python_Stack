from django.db import models


class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    desc = models.TextField(default="old dojo")
    state = models.CharField(max_length=2)

    def __str__(self):
        return f"<Dojo object: {self.name}, {self.city}, {self.state} ({self.id})>"


class Ninjas(models.Model):
    dojo = models.ForeignKey(
        Dojos, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"<Ninja object: {self.dojo}, {self.first_name}, {self.last_name} ({self.id})>"
