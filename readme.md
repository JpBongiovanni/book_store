Deployed Web Page: https://christianbookcatalog.herokuapp.com/
Github: https://github.com/JpBongiovanni/book_store

Website Instructions: Navigate to the "upload new products" page. Copy The entirety of the text in static/product_app/json/products.json on github page and paste
it into the text area. Hit submit. The contents of the Json file will be added to the database and you will be redirected to the home page. Improper
Json format will result in the upload new products page being reloaded. Items will not duplicate on submission.

How to Run:



Comments:
More detailed comments are left in my views.py and settings.py files. These comments 

Known Bugs:
1. Auto escape in my HTML is working on some pages but not in others. The Lego trademark symbol renders correctly in the main page, but not 
on its own page or search result despite auto escape being added to the HTML
2. I am still working on a way for an "alert" function to pop up when improper Json is entered into the text area


Sources Used:
1. Search Vector Documentation - https://docs.djangoproject.com/en/3.2/ref/contrib/postgres/search/
2. Auto Escaping Documentation - https://code.djangoproject.com/wiki/AutoEscaping