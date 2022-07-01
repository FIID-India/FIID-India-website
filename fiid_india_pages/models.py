from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from io import BytesIO
import sys
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile


# File type choices used in File model
FILE_TYPE = (
    ("Report", "Report"),
    ("Newsletter", "Newsletter"),
    ("Others", "Others"),
)

PAGE_LIST = (
    ("About", "About"),
    ("Objectives", "Objectives"),
    ("Programmes", "Programmes"),
)


# Carousel Model
class Carousel(models.Model):
    heading = models.CharField(max_length=300)
    text = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/carousel/')

    # Compress Image on Upload
    def save(self):
        # Opening the uploaded image
        im = PIL.Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1024, 768))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Carousel, self).save()

    def __str__(self):
        return(self.heading)



# Image model linked to pages
class Image(models.Model):
    page = models.CharField(choices=PAGE_LIST, max_length=200)
    image = models.ImageField(upload_to='images/pages/')

    def save(self):
        # Opening the uploaded image
        im = PIL.Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1024, 768))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Image, self).save()

    def __str__(self):
        return str(self.page)


# Contact Form model to save messages in database send by others to the admin using contact form
class Contact (models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    date_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"From : "+self.email)


# File model to upload files like newsletters, reports etc.
class File(models.Model):
    title = models.CharField(max_length=300)
    date_and_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    file = models.FileField(upload_to='files/')
    file_type = models.CharField(
        max_length=20, choices=FILE_TYPE, default='Newsletter')

    def __str__(self):
        return str(self.title)



# To delete images when the instace is deleted in Carousel model
@receiver(pre_delete, sender=Carousel)
def Carousel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)


# To delete images when the instace is deleted in Image model
@receiver(pre_delete, sender=Image)
def Image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
