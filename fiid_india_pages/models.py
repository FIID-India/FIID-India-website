from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)

class Summary(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE)
    summary = models.TextField()

    def __str__(self):
        return str(self.page)
