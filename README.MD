# Learning about Django Web Framework

### Installing Django
```pip install Django```

### Checking Version
```python -m django --version```

### Project
- A basic poll app
- It’ll consist of two parts: <br>
-- A public site that lets people view polls and vote in them. <br>
-- An admin site that lets you add, change, and delete polls. <br>

## Procedure

### Part 1 - Basic Request & Response Flow
- Auto-generate some code that establishes a Django project <br>
```django-admin startproject mysite``` <br>
- Change Directory to mysite folder <br>
```cd mysite``` <br>
- Run the Django webserver <br>
```python manage.py runserver``` <br>
OR <br>
```python manage.py runserver 8080``` <br> 
- Go to http://127.0.0.1:8000/ <br>
![Django server started](/images/ss1.png?raw=true "Django server started")

The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases. <br>

- To create your app, make sure you’re in the same directory as manage.py and type this command: <br>
```python manage.py startapp polls```

- Write your first view <br>
Open the file polls/views.py and write the code. <br>

- To call the view, we need to map it to a URL <br>
Create a file called urls.py and write the code. <br>

- Point the root URLconf at the polls.urls module <br>
In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list. <br>

- You have now wired an index view into the URLconf. Verify it’s working with the following command: <br>
```python manage.py runserver```

- Go to http://localhost:8000/polls/ in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which you defined in the index view.

### Part 2 - Models & the Admin site
- Open mysite/settings.py
Change the DB settings if required. Set the Timezone as per your location (TIME_ZONE = 'EST'), also have a look at the INSTALLED_APPS. <br>
- Then, these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command: <br>
```python manage.py migrate```
- Creating Models <br>
    1. In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question. <br>

    2. Edit the polls/models.py file <br>
    Create the models for Question and Choice
- Activating Models <br>
    1. The PollsConfig class is in the polls/apps.py file, get the dotted path ```polls.apps.PollsConfig``` <br>

    2. Edit the mysite/settings.py file and add the dotted path under INSTALLED_APPS. <br>

    3. Then run the command: ```python manage.py makemigrations polls``` <br>
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
- The sqlmigrate command takes migration names and returns their SQL: <br>
```python manage.py sqlmigrate polls 0001```
- Now, run migrate again to create those model tables in your database: <br>
```python manage.py migrate```
- Playing with the API <br>
-- Invoke it <br>
```python manage.py shell``` <br>
-- Explore it <br>
From the shell, create questions and choices and explore the CRUD features.
- Creating an admin user <br>
```python manage.py createsuperuser``` <br>
Username: admin <br>
Email address: admin@example.com <br>
The final step is to enter your password. You will be asked to enter your password twice. <br>
    1. Start the development server <br>
    ```python manage.py runserver```

    2. Go to  http://127.0.0.1:8000/admin/ <br>

    3. Login using the credentials <br>

    4. Make the poll app modifiable in the admin [Edit the polls/admin.py file] <br>

    5. Explore the free admin functionality <br>

    6. Click “Questions”. Now you’re at the “change list” page for questions. This page displays all the questions in the database and lets you choose one to change it. <br>

    7. Can also view the history of changes made. <br>

### Part 3 - Views & Templates
- In our poll application, we’ll have the following four views: <br>

    1. Question “index” page – displays the latest few questions. <br>
    2. Question “detail” page – displays a question text, with no results but with a form to vote. <br>
    3. Question “results” page – displays results for a particular question. <br>
    4. Vote action – handles voting for a particular choice in a particular question. <br>

- Write some more views in polls/views.py <br>
- Wire these new views into the polls/urls.py module by adding the respective path() calls. <br>
- Run the server again ```python manage.py runserver``` <br>
- Try "/polls/", "/polls/34/results/" and "/polls/34/vote/" <br>
- Write views that actually do something by editing polls/views.py <br>
- Use Django’s template system to separate the design from Python by creating a template that the view can use. <br>
- Create templates directory inside polls directory, and inside it create index.html file. <br>
- Edit the index.html file with desired HTML code. <br>
- Update our index view function in polls/views.py to use the template. <br>
- Load the page by pointing your browser at '/polls/' .<br>
- A shortcut in Django to return an HttpResponse object of a given template rendered with given context is by using render() . <br>
- Raising a 404 Error: The view raises the Http404 exception if a question with the requested ID doesn’t exist. <br>
- Above method requires to import Http404 and then use try...catch method. There exists a shortcut too in Django using get_object_or_404 . <br>
- Update the polls/detail.html file to render the view as desired (i.e., Display Questions alongwith choices). <br>
- Remove the hardcoded URLs in templates. <br>
- Edit the URLs in polls/urls.py if required. <br>
- Add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name = 'polls', to set the application namespace. <br>

### Part 4 - Forms & Generic Views
- Update our poll detail template (“polls/detail.html”), so that the template contains an HTML ```<form>``` element. <br>
- Create a Django view that handles the submitted data and does something with it. <br>
- Edit the polls/views.py and create a real implemntation of vote() and results() function. <br>
- Create a polls/results.html template. <br>
- Now, go to /polls/1/ in your browser and vote in the question. You should see a results page that gets updated each time you vote. If you submit the form without having chosen a choice, you should see the error message. <br>
- Use generic views provided by Django and amend the URLconf and Views.

### Part 5 - Testing
- Creating Automated Tests for our Application <br>
- Identifying bugs: ```python manage.py shell``` <br>
- Create a test to expose the bug. (Automated test) in polls/tests.py <br>
- Run the tests: ```python manage.py test polls``` <br>
- Fixing the bug: Amend the method in models.py <br>
- Run the test again. <br>
- Add some more comprehensive tests. <br>
- Run the test again. <br>
- Test a View: ```python manage.py shell``` <br>
- Setup_test_environment() <br>
- Amend the get_queryset() method and change it so that it also checks the date by comparing it with timezone.now() <br>
- Test our new view <br>
- For Testing, we need to create Questions with dates in the past and future, and checking that only those that have been published are listed. So, modify the IndexView, DetailView and ResultsView queryset() to reflect the same. <br>
- Create the Tests in polls/tests.py <br>
- Add more Tests as required for all the views [IndexView, DetailView and ResultsView]. <br>


### Part 6 - Static Files
- Create a directory "static" inside polls directory. <br>
- Then, create style.css inside static folder. <br>
- Modify the index.html file to include style.css <br>
- Run the server and observe changes. <br>


### Part 7 - Customizing the Admin site
- Customize the admin form. <br>
- Go to admin.py, add forms, fieldsets, etc. <br>
- It’d be better if you could add a bunch of Choices directly when you create the Question object. SO, edit the polls/admin.py accordingly. <br>
- Also, edit the "Select question to change" page. Add Date Published column and published recently columns. Also, add filter by date/past 7 days/monnth/year functionality. Additionally a search functionality could be added. All this is done in admin.py file. <br>
- Customize the admin look and feel using Django's template system. <br>
- Open mysite/settings.py file and edit the DIRS option in the TEMPLATES setting. <br>
``` 'DIRS': [BASE_DIR / 'templates'], ``` <br>
- Create admin directory inside templates. <br>
- Run this command: ```python -c "import django; print(django.__path__)"``` <br>
- Copy the ```admin/base_site.html``` from ```django/contrib/admin/templates``` to the newly created admin directory. <br>
- Also, similarly modify the index.html file, if desired. <br>

### Screenshots
![Django Poll App](/images/ss2.png?raw=true "Django Poll App")
![Django Poll App](/images/ss3.png?raw=true "Django Poll App")
![Django Poll App](/images/ss4.png?raw=true "Django Poll App")
![Django Poll App](/images/ss5.png?raw=true "Django Poll App")
![Django Poll App](/images/ss6.png?raw=true "Django Poll App")
![Django Poll App](/images/ss7.png?raw=true "Django Poll App")

### References
- https://docs.djangoproject.com/en/4.1/intro/tutorial01/