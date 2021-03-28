# dj-restaurants

> Build restaurants app via Django framework
- Python 3.4, Django 1.7

### Quick start
```bash
# init project
source activate django-env
cd dj-restaurants 
django-admin.py startproject mysite

# init app
cd dj-restaurants/mysite && python manage.py startapp restaurants

# run the app
export PYTHONPATH=/Users/$USER/dj-restaurants/
cd dj-restaurants/mysite
python manage.py runserver
```

### Endpoints
- http://127.0.0.1:8000/here
- http://127.0.0.1:8000/2/plus/2/
- http://127.0.0.1:8000/menu