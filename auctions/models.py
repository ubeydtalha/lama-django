from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Auctions(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE) #Makalenin sahipleri user tablosundan çekiliyor
    name = models.CharField(max_length=50) #Makale ismi
    feature = RichTextField(verbose_name="Özellikler")
    created_date = models.DateField(auto_now_add=True)#Oluşturulma zamanı
    auction_image = models.FileField(blank=True,null= True,verbose_name="Foto")

    def __str__(self):
        return self.name