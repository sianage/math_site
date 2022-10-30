from django.db import models


class Chapter(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class Section(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"