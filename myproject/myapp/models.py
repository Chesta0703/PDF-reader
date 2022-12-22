from django.db import models

# Create your models here.




class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    text = models.TextField()
    
    class Meta:
        app_label = 'myapp'
