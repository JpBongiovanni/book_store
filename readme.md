Comments:
More detailed comments are left in my views.py and settings.py files. These comments 

Deployed Web Page: https://christianbookcatalog.herokuapp.com/
Github: https://github.com/JpBongiovanni/book_store

Website Instructions: Navigate to the "upload new products" page. Copy The entirety of the text in static/product_app/json/products.json on github page and paste
it into the text area. Hit submit. The contents of the Json file will be added to the database and you will be redirected to the home page. Improper
Json format will result in the upload new products page being reloaded. Items will not duplicate on submission.

to access a specific ID number, you can use the search function at the top, or enter the id into the url: https://christianbookcatalog.herokuapp.com/single_item/<idnumber>

How to Run:
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

Known Bugs:
1. I am still working on a way for an "alert" function to pop up when improper Json is entered into the text area


Sources Used:
1. Search Vector Documentation - https://docs.djangoproject.com/en/3.2/ref/contrib/postgres/search/
2. Auto Escaping Documentation - https://code.djangoproject.com/wiki/AutoEscaping
3. Help with breaking down the steps to run off a git clone command - https://stackoverflow.com/questions/37094032/how-to-run-cloned-django-project
4. Django secret-key generator - https://miniwebtool.com/django-secret-key-generator/
5. Simple steps to create postgreSQL db - https://www.section.io/engineering-education/django-app-using-postgresql-database/