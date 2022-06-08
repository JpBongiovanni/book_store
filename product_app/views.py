from django.shortcuts import render, redirect
from .models import SaleItem
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q
import json

# I imported pyautogui to make use of the "alert" function it had for my add_more_product def. However, It would not work in deployment. I left the code
# commented out in order to revisit it
# import pyautogui as pag


#renders home page with correct context
def index(request):
    
    context = {
        "items": SaleItem.objects.all(),
    }
        
    return render(request, 'index.html', context)

#renders upload products page for uploading more products
def upload_products(request):
    return render(request, "upload_products.html", {})

#renders the single item page for individual items. 
def single_item(request, item_id):

    try:
        context = {
            "item": SaleItem.objects.get(id=item_id)
        }
        
        return render(request, "single_item_page.html", context)
    
    except Exception as e:
        print(e)
        return redirect('/')

#The add_more_product function makes use of the python json library. Because this application would only be used in the setting of a specific company, 
#the function only works if the POST data is JSON format, with the correct key/value pairs for that company. In this case it mirrors the Json file that
#was provided for me in this assignment. 
#the User navigates to the upload products page, and simply copies and pastes the entire contents of the Json file into the text area. On submission
#the the method will convert the json into a python dictionary which will be read and added to the database ignoring duplicates.
#Because this application would only be used by employees, no authentication was added to the form, and no checks were put in place to preven malicious 
#code from being submitted. 
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
                    # itemId = item['id']
                    # pag.alert(text=f'{"Item Id: " + itemId + " already exists"}', title="Duplicate Error")
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
            # pag.alert(text="Please format your text to Json format", title="Improper Format")
            return redirect('/upload_products')
        
    except Exception as e:
        print(e)
        # pag.alert(text="Please format your text to Json format", title="Improper Format")
        return redirect('/upload_products')

'''The methods below are for buttons and links'''

#the basic search function makes use of SearchVector and SearchQuery. Search vector allows me to condense by code a bit by adding multiple fields to the 
#search separated by a comma in line 87 (although in this case I'm only searching one field). Search Vector than puts the results in a python list that
#changes in size based on the number of words in the search query. the search "NKJV Bible" would yeild ['NKJV', 'Bible'] as my search results. Because
# of this I need the for loop in line 88 to appened each QuerySet from the database to my context
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
    
#for search ID I used Q search instead of Search Vector. Q is very specific with the queries it taks, and because the requirements of the test project 
#stated that individual IDs must be searchable, I went in this direction expecting the User to search for only one product at a time. 
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

#Basic delete function to enable the user to delete items from the database. Because this type of appication would only be used by engineers within the company
#and not users, I did not feel the need to hide this behind authentication
def delete(request, item_id):
    SaleItem.objects.get(id=item_id).delete()
    
    return redirect('/')