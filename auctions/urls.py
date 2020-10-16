from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "auctions"

urlpatterns = [
    path('', views.auctions, name="auctions"),
    path('create_auction/', views.create_auction, name="create_auction"),
    path('dashboard/', views.dashboard , name="dashboard"),
    path('auction/<int:id>', views.detail , name="detail"),
    path('edit/<int:id>',views.edit,name = "edit"),
    path('delete/<int:id>',views.delete,name = "delete"),
   
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)