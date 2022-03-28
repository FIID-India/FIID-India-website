from distutils.command.upload import upload
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class Carousel(models.Model):
    heading = models.CharField(max_length=300)
    text = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/carousel/')

    def __str__(self):
        return(self.heading)

class Page(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)

class Image(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/pages/')

    def __str__(self):
        return str(self.page)

class Summary(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE)
    summary = models.TextField()

    def __str__(self):
        return str(self.page)

class Paragraph(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE)
    paragraph = models.TextField()

    def __str__(self):
        return str(self.page)

@receiver(pre_delete, sender=Carousel)
def Carousel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)


@receiver(pre_delete, sender=Image)
def Image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)