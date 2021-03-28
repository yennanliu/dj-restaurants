# dj-restaurants

> Build restaurants app via Django framework
- Python 3.4, Django 1.7

### Quick start
```bash
# run the app
export PYTHONPATH=/Users/$USER/dj-restaurants/
cd dj-restaurants/mysite
python manage.py runserver
```

### Operation
```bash
# init project
source activate django-env
cd dj-restaurants 
django-admin.py startproject mysite

# init app
cd dj-restaurants/mysite && python manage.py startapp restaurants

# check if DB model is correct
python manage.py check

# make migration
python manage.py makemigrations restaurants
```

### Structure
```
├── README.md
├── doc
│   └── progress.md
├── mysite
│   ├── db.sqlite3
│   ├── manage.py
│   ├── mysite
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   ├── restaurants
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── templates
│       ├── math.html
│       └── menu.html
└── requirements.txt
```

### Endpoints
- http://127.0.0.1:8000/here
- http://127.0.0.1:8000/2/plus/2/
- http://127.0.0.1:8000/menu