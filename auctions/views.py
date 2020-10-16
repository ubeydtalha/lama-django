from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import AuctionsForm
from django.contrib import messages
from .models import Auctions
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    content = {
        "deneme":[1,2,3],
    }
    return render(
        request,
        template_name="index.html",
        context=content)

def about(request):
    return render(request,template_name="about.html")    


@login_required(login_url= "user:login_user")
def dashboard(request):
    auctions = Auctions.objects.filter(author = request.user)
    context = {
        "auctions":auctions,
    }
    return render(request,template_name="dashboard.html",context=context) #

@login_required(login_url= "user:login_user")
def create_auction(request):
    form = AuctionsForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        
        
        auctions =  form.save(commit=False)
        auctions.author = request.user
       
        auctions.save()
        messages.success(request,"Created")
        return redirect("index")



    return render(request,template_name="create_auctions.html",context={"form":form})          

def detail(request,id):
    #auction = Auctions.objects.filter(id = id)
    auction = get_object_or_404(Auctions,id=id)
    return render(request,"detail.html",{"auction":auction})


def auctions(request):

    auctions = Auctions.objects.all()
    context = {"auctions":auctions}
    return render(request,"auctions.html",context= context)

@login_required(login_url= "user:login_user")
def edit(request,id):

    auction = get_object_or_404(Auctions,id=id)   

    form = AuctionsForm(request.POST or None,request.FILES or None,instance=auction)

    if form.is_valid():
        auction =  form.save(commit=False)
        auction.author = request.user
        auction.save()
        messages.success(request,"Updated")
        return redirect("index")

    context = {"form":form}


    return render(request,"edit.html",context)

@login_required(login_url= "user:login_user")
def delete(request):

    auction = get_object_or_404(Auctions,id=id)

    auction.delete() 

    messages.warning(request,"Makale silindi")

    return redirect("dashboard")   