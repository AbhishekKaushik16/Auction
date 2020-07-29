from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.shortcuts import redirect
from django.db.models import Max

from .models import User,Listings,Bids,Comment


def index(request):
    if request.user.is_authenticated :
        return render(request, "auctions/index.html",{
            "listings" : Listings.objects.all()
        })
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def categories(request):
    categories = Listings.objects.order_by('category').values_list('category').distinct()
    return render(request, "auctions/categories.html", {
        "categories" : categories
    })

def categorical_listing(request, category):
    listing = Listings.objects.filter(category = category).all()
    return render(request,"auctions/index.html",{
        "listings": listing
    })


def watchlist(request):
    listings = Listings.objects.all().filter(watchlist=True)
    return render(request, "auctions/index.html", {
        "listings": listings
    })

def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        price = request.POST["price"]
        category = request.POST["category"]
        description = request.POST["description"]
        listed_by = request.user.username
        created_on = datetime.now()
        listing = Listings(item_name=title,description=description,item_price=price,listed_by=listed_by,category=category,date_added=created_on)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html")


def listings(request, id):
    args = Bids.objects.all()
    max_bid = args.order_by("-amount").first()
    listing = Listings.objects.get(pk=id)
    comments = Comment.objects.filter(post=listing).all()

    if request.method == "POST" and 'place-bid' in request.POST :
        bid_value = request.POST["bid_value"]
        person_name = request.user.username
        listing_id = id

        bid = Bids(person_name=person_name, listing_id=listing,amount=bid_value)
        bid.save()
        args = Bids.objects.all()
        max_bid = args.order_by("-amount").first()
        return render(request, "auctions/listings.html",{
            "message" : "Your bid was placed successfully",
            "listings" : listing,
            "max_bid" : max_bid
        })
    elif 'post-comment' in request.POST:
        comment = request.POST['comment']
        name = request.user.username
        new_comment = Comment(post=listing,name=name,body=comment)
        new_comment.save()
        comments = Comment.objects.filter(post=listing).all()

    return render(request, "auctions/listings.html", {
        "listings" : listing,
        "max_bid" : max_bid,
        "comments": comments
    })


def change_watchlist(request, id):
    listing = Listings.objects.get(id_no=id)
    if listing.watchlist == True:
        listing.watchlist = False
    else:
        listing.watchlist = True
    listing.save()
    return redirect('listings', id=id)