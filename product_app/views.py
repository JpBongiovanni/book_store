from cgitb import text
from django.shortcuts import render, redirect
from .models import SaleItem
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q
import json
import re
import pyautogui as pag


def add_more_product(request):
    try:
        if request.method == "POST":
            new_product = request.POST["json_txt"]
            
        json_products = json.loads(new_product)
        
        records = json_products["records"]
        try:
            for item in records:
                SaleItem.objects.filter(id__contains=item['id'])
                exists = SaleItem.objects.filter(id__contains=item['id'])
                    
                if exists:
                    itemId = item['id']
                    pag.alert(text=f'{"Item Id: " + itemId + " already exists"}', title="Duplicate Error")
                    continue
                else:
                    SaleItem.objects.create(
                        title = item['title'],
                        isbn13 = item['isbn13'],
                        isbn = item['isbn'],
                        image = item['image'],
                        id = item['id'],
                        link = item['link'],
                        customer_rating = item['customer_rating'],
                    )
            return redirect('/')
        except Exception as e:
            print(e)
            pag.alert(text="Please format your text to Json format", title="Improper Format")
            return redirect('/upload_products')
        
    except Exception as e:
        print(e)
        pag.alert(text="Please format your text to Json format", title="Improper Format")
        return redirect('/upload_products')

def upload_products(request):
    return render(request, "upload_products.html", {})

def index(request):
    context = {
        "items": SaleItem.objects.all(),
    }
        
    return render(request, 'index.html', context)

def single_item(request, item_id):
    
    #for some reason if the url has <int:0---0 as an ID it gets shortened to a number that starts with a positive integer. 
    #the url needs to have a string variable in order to work properly. The same is true for any def that requires a specific
    #value in the url.
    
    try:
        context = {
            "item": SaleItem.objects.get(id=item_id)
        }
        
        return render(request, "single_item_page.html", context)
    
    except Exception as e:
        print(e)
        return redirect('/')

def search(request):
    if request.method == "GET":
        search = request.GET["search"],
        print(search)
        searchList = search[0].split()
        results = []
        for searchWord in searchList:
            searchRes = SaleItem.objects.annotate(search=SearchVector('title')).filter(search=SearchQuery(searchWord, search_type='phrase'))
            
            results.append(searchRes)
        print(results[0])
        print(SaleItem.objects.all())
        context = {
            "items": results[0],
            "search": search[0],
        }
        return render(request, 'search_results.html', context)
    
def searchId(request):
    if request.method == "GET":
        search = request.GET["searchId"],
        print(type(search))
        searchIdList = SaleItem.objects.filter(Q(isbn13__icontains=search[0])|Q(isbn__icontains=search[0])|Q(id__icontains=search[0]))
        
        context = {
            "items": searchIdList,
            "search": search[0]
        }
        
        return render(request, "search_results.html", context)
    
def delete(request, item_id):
    SaleItem.objects.get(id=item_id).delete()
    
    return redirect('/')