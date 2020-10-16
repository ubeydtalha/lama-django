from django import forms
from .models import Auctions



class AuctionsForm(forms.ModelForm):
    
    class Meta:
        model = Auctions
        fields = ["name","feature","auction_image"]
