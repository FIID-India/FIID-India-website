from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from io import BytesIO
import sys
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile

FILE_TYPE =(
    ("Report", "Report"),
    ("Newsletter", "Newsletter"),
    ("Others", "Others"),
)

class Carousel(models.Model):
    heading = models.CharField(max_length=300)
    text = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/carousel/')

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

class Page(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)

class Image(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
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

class Contact (models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    date_and_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"From : "+self.email)

class File(models.Model):
    title = models.CharField(max_length=300)
    date_and_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    file = models.FileField(upload_to='files/')
    file_type = models.CharField(max_length=20, choices=FILE_TYPE, default='Newsletter')

    def __str__(self):
        return str(self.title)

class Subscriber(models.Model):
    full_name = models.CharField(max_length=400)
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.full_name)

@receiver(pre_delete, sender=Carousel)
def Carousel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)


@receiver(pre_delete, sender=Image)
def Image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)