# Khudegobeshok Backend

This is the backend for khudegobeshok platform.

## Local development
- Clone the project
- Make a virtual environment for the project (Optional, but preferred)
- Install all the dependencies from requirements.txt `pip install requirements.txt`
- Install PostgreSQL.
- Set up the environment variable - SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD
- Navigate to the project directory and make migrations `python manage.py makemigrations`
- Run the project `python manage.py runserver`
- To make a superuser `python manage.py createsuperuser`
- Have fun!