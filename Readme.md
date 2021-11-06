Guide to learn about the Django Framework

Installation of django
1. install python with major version 3
2. Create new venv using python3 -m venv ./venv
3. install django in vevn using pip install django
4. Create the Starter project using django-admin startproject vt .
5. Test by running server using python manage.py runserver
6. Create the new pages app using python manage.py startapp pages
7. Add the static file in root of the folder using the command python manage.py collectstatic
7.1 Add the root location of static file using STATIC_ROOT = os.path.join(BASE_DIR, 'static')
7.2 Add the static file directory for command in point 7 lookup using STATICFILES_DIRS = [os.path.join(BASE_DIR, 'vt/static')]
7.3 Update the settings.py 
8. install postgres from postgre website.
9. set password and create new database.
