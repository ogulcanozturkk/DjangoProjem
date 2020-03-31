from django.db import models

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(blank=True,max_length=255)
    company = models.CharField(blank=True,max_length=150)
    address = models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(max_length=50)
    smtpserver = models.CharField(blank=True,max_length=20)
    smtpemail = models.CharField(blank=True,max_length=20)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    aboutus = models.TextField()
    contact = models.TextField()
    referances = models.TextField()
    status = models.CharField(  max_length=10,choices=STATUS)
    create_at = models.DateTimeField (auto_now_add=True)
    update_at = models.DateTimeField (auto_now=True)



    def __str__(self):
        return self.title
