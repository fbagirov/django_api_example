This is a sample Python Django API app, that is based on a simple Django framework (non-Django REST framework). The Django version used is 2.2.11. For a database it uses the default SQLite. 

Please note that if you would like to start your own project and follow along the code, you can do it with the following command(from the command line, make sure you are in the same folder as manage.py file): 

> django-admin startproject yourprojectname

Whenever you need to start a new app, you can do it with the following command(from the command line, make sure you are in the same folder as manage.py file): 

> python manage.py startapp yourappname

Whenever you create a new class in your model, run the following command(from the command line, make sure you are in the same folder as manage.py file): 

> python manage.py makemigrations

Before running the code, perform the commands below.:
1. Create and activate a virtual environment 
2. Install the requirements.txt into the virtual environment using the following command (this app uses Django version 2.2.11): 

> pip install -r requirements.txt

3. Run the migrate command: 

> python manage.py migrate

4. Create a superuser: 

> python manage.py createsuperuser

(the username/password for superuser in this app is admin/admin)

5. Run the app (from the command line, make sure you are in the same folder as manage.py file): 

> python manage.py runserver

6. In your browser, go to the following address: "127.0.0.1:8000" or "localhost:8000"

7. To access all leads in the database, go to the following address: 

8. To access a specific lead in the database by the user id, go to the following address: 

9. To shut down the application, in your command shell, use CTRL+c command. 
