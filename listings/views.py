from django.http.response import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from listings.choices import price_choices,bedroom_choices,state_choices

from realtors.models import Realtor
from .models import Listing
import pages

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(listings, 6)
    page = request.GET.get('page') # This is the url for pagination ex : /page=2
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
        'listing' : listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_listings = Listing.objects.all().order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_listings = queryset_listings.filter(description__icontains=keywords)

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_listings = queryset_listings.filter(city__iexact=city)

    #State
    if 'state' in request.GET:
        print(request.GET)
        stat = request.GET['state']
        print(stat)
        if stat:
            queryset_listings = queryset_listings.filter(state__icontains=stat)
    
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_listings = queryset_listings.filter(bedrooms__lte=bedrooms)

    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_listings = queryset_listings.filter(price__lte=price)

    context = {
        'queryset_listings': queryset_listings, 
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'values' : request.GET
    }
    
    return render(request, 'listings/search.html', context)


