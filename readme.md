### Comments:
More detailed comments are left in my views.py and settings.py files. These comments 

### Deployed Web Page: https://christianbookcatalog.herokuapp.com/
### Github: https://github.com/JpBongiovanni/book_store

### Website Instructions: 
Navigate to the "upload new products" page. Copy The entirety of the text in static/product_app/json/products.json on github page and paste
it into the text area. Hit submit. The contents of the Json file will be added to the database and you will be redirected to the home page. Improper
Json format will result in the upload new products page being reloaded. Items will not duplicate on submission.

to access a specific ID number, you can use the search function at the top, or enter the id into the url: https://christianbookcatalog.herokuapp.com/single_item/<idnumber>

### How to Run:
1. Make a directory to house your project
2. navigate into that directory and create a python virtual environment using the command "python -m venv venvName"
3. turn on virtual environment with the command "source venvName/scripts/activate" (GitBash, willm be a different command for Mac users)
4. install Django in your virtual environment with the command "pip install django"
5. on my github fork and clone the repository into the directory you created
6. Navigate into the directory
7. install all project dependencies with command "pip install -r requirements.txt
8. Open up files in IDE of your choosing and navigate to the settings.py file
9. Open a browser and go to https://miniwebtool.com/django-secret-key-generator/ to generate a django secret key
10. In the settings.py file replace the secret key value with the string you generated using the webtool (On deployment you will want to hide this in with an env variable)
11. Scroll down the settings.py page to the DATABASES dictionary. Comment out the entire dictionary and replace it with the standard sqlite3 database
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }

    this might cause the search function not to run correctly, in which case you will need to create your own PostgreSQL database and change the database values to the following:

            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': 'db_name',
                    'USER': 'name',
                    'PASSWORD': '',
                    'HOST': 'localhost',
                    'PORT': '',
                }
            }

12. in your git bash terminal or other command line run "python manage.py makemigrations" then "python manage.py migrate" 
13. Finally, run "python manage.py runserver" and navigate in your browser to localhost:8000

14. if the "Search Title" function isn't working properly, it is because it makes use of search vector which only runs on a PostgreSQL database. Go back to step 11 and copy and paste the second Database dictionary over the sqlite3 dictionary
15. You will need to create a database in postgreSQL.
    a. install postgreSQL on your machine https://www.postgresql.org/download/windows/
    b. Open up SQL Shell (psql) via your start menu, once open the shell will prompt you for information. Hit enter to use defaults. lastly enter the password you used for the installation of postreSQL
    c. Enter the command "create database nameOfDatabase"
16. Go back to your terminal/command line and run "python manage.py createsuperuser"
17. run python "manage.py makemigrations book_store" followed by "python manage.py migrate", and then finally "python manage.py runserver"
18. In your browser open localhost:8000
19. To populate your database, navigate to static/product_app/json/products.json and copy the contents of that file in its entierety. Navigate to the upload new products page and paste the json string into the text area and hit submit.

### Known Bugs:
1. I am still working on a way for an "alert" function to pop up when improper Json is entered into the text area


### Sources Used:
1. Search Vector Documentation - https://docs.djangoproject.com/en/3.2/ref/contrib/postgres/search/
2. Auto Escaping Documentation - https://code.djangoproject.com/wiki/AutoEscaping
3. Help with breaking down the steps to run off a git clone command - https://stackoverflow.com/questions/37094032/how-to-run-cloned-django-project
4. Django secret-key generator - https://miniwebtool.com/django-secret-key-generator/
5. Simple steps to create postgreSQL db - https://www.section.io/engineering-education/django-app-using-postgresql-database/
6. Various sites to learn more about Python Json interaction:
    https://simplejson.readthedocs.io/en/latest/
    https://docs.python.org/3/library/json.html
    https://stackoverflow.com/questions/19483351/converting-json-string-to-dictionary-not-list


#### Assignment Questions

How does your system work? (if not addressed in comments in source)

    See comments in views.py and settings.py files

How will your system perform with a 1 product in file? 10 products in file? 100 products in file?

    PostgreSQL as a DB can handle large amounts of data and is incredibley popular. Heroku provides its own Postgres database for programmers to use when they deploy their projects. For a small hobby site with not many files, the free tier is fine. However, as the amount of data grows so does the cost. You will need more storage and RAM to access that storage and Heroku is happy to give it to you for a price. Right now the website could handle a large number of products because it's all text with links to other websites, so while I may need to increase the horsepower of the webpage to scale with multiple users, the provided database management from heroku would not need to scale as quickly. 

How will your system perform with 100 users? 10000 users? 1000000 users?

    Similar to my previous answer, right now my deployed site is only running off of 1 free Dyno on heroku. If more than a few people were to use it at once, it would crash. In order to scale it properly I would need to somehow analyze how much traffic its getting and increase the number of dynos for the server. 

What documentation, websites, papers, etc did you consult in doing this assignment?

    see "Sourses used" section

How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?

    This project took around 2 days (about 16 hours of work). A big chunk of that was fighting with heroku for deployment, and figuring out how to upload formatted Json files into the database. Ultimately the solution was simple and would only take a few minutes to implement now, but trying various methods and reaching many dead ends was time consuming. 

    If I had unlimited time, I would first focus on the search functionality. Its not incredibly sophisticated, and when it comes to thousands of products that could be added, users will need more filters to find what they want. I would also spend more time on making the user interface more intuitive to make sure the user does not need to spend a lot of time learning how our site works.

If you were to critique your code, what would you have to say about it?

    I would say that my code is clean, organized, and easy to read. However, due to time constraints the options used to create some of the functions (specifically the search functions) might not be the most optimal. I tried my best to not repeat myself, but there is probably a function or method out there that could be utilized for both search fields. 