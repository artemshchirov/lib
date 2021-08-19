# For work in Jupyter

**in settings.py:**

`os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"`

**install:**

`pip install django-extensions`

**INSTALLED_APPS:**

```python
INSTALLED_APPS =  [

         ''''
    'django_extensions',
        '''''
]
```

**Start:**

`alias jns="python3 manage.py shell_plus --notebook"`

`$ python3 manage.py shell_plus --notebook`
