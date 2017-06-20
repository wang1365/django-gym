# django-learning
Django


## 1. Prerequisite
    To connect to mysql, Django depends on mysqldb lib provided by mysqlclient:
        https://github.com/PyMySQL/mysqlclient-python

    To install it:
        For windows:
            Download wheel from http://www.lfd.uci.edu/~gohlke/pythonlibs and install it
        For Ubuntu:
            `sudo apt-get install python-dev libmysqlclient-dev` # Debian / Ubuntu
            `pip install mysqlclient`



## 2. Deployment
    We use uwsgi to run the application. For a real productive deployment, we also need to use
    nginx as a HTTP reverse proxy.
    2.1 Install uWSGI
        For Ubuntu:
            Install c header compiler dependency: `apt-get install build-essential python-dev`
            Install uswgi via pip: `pip install uwsgi`
    2.2 Run Django application with uwsgi
        `uwsgi --http :8080 --wsgi-file djangoproject/wsgi.py`

