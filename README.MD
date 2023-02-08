# Learning about Django Web Framework

### Installing
```pip install Django```

### Checking Version
```python -m django --version```

### Project
- A basic poll app
- It’ll consist of two parts: <br>
-- A public site that lets people view polls and vote in them. <br>
-- An admin site that lets you add, change, and delete polls. <br>

### Procedure
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

The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

- To create your app, make sure you’re in the same directory as manage.py and type this command: <br>
```python manage.py startapp polls```

- Write your first view <br>
Open the file polls/views.py and write the code.

- To call the view, we need to map it to a URL <br>
Create a file called urls.py and write the code.

- Point the root URLconf at the polls.urls module <br>
In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list.

- You have now wired an index view into the URLconf. Verify it’s working with the following command: <br>
```python manage.py runserver```

- Go to http://localhost:8000/polls/ in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which you defined in the index view.

TEST

### References
- https://docs.djangoproject.com/en/4.1/intro/tutorial01/