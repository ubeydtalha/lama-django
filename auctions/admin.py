from django.contrib import admin

from .models import Auctions
# Register your models here.

@admin.register(Auctions)
class AuctionsAdmin(admin.ModelAdmin):
    
    list_display = ["name","author"] # Listede gösterilecek özellikler

    list_display_links = ["name","author"] #Üzerine tıklandığında tıklanılan makaleye gidecek özellikler

    search_fields = ["name"] # Arama yapmak için gerekli parametre - İsim'e göre arama yapabileceğiz

    list_filter=["created_date"] # Filtreleme özelliği - Tarihe göre filtreleme
    
    class Meta:
        model = Auctions

