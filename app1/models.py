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

class AlgChapter(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class AlgSection(models.Model):
    chapter = models.ForeignKey(AlgChapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class CalcChapter(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class CalcSection(models.Model):
    chapter = models.ForeignKey(CalcChapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class DMChapter(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class DMSection(models.Model):
    chapter = models.ForeignKey(DMChapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class StatsChapter(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class StatsSection(models.Model):
    chapter = models.ForeignKey(StatsChapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class LAChapter(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class LASection(models.Model):
    chapter = models.ForeignKey(LAChapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"