# django-learning

## 1. MySQL support
To connect to mysql, Django depends on mysqlmysqldb lib provided by *[mysqlclient](https://github.com/PyMySQL/mysqlclient-python)*.

#### 1.1 Install mysqlclient 
* For windows, download wheel from *[Unoffical PYPI](http://www.lfd.uci.edu/~gohlke/pythonlibs)* and install it.  
* For Ubuntu, execute the following commands:  
>> `sudo apt-get install python-dev libmysqlclient-dev`   
`pip install mysqlclient`

#### 1.2 Django setting for mysql 
Modify project setting file `setting.py`:  
```
DATABASES = {
    'default': {
        # 'ENGINE': 'mysql.connector.django',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'I321761',
        'USER': 'root',
        'PASSWORD': '******',
        'HOST': '10.128.184.199',
        'PORT': '3306',
    },
}
```

## 2. Deployment
We use **uwsgi** to run the application, here we use **[uWSGI](https://uwsgi-docs.readthedocs.io)** as uwsgi server. For a real productive deployment, we also need to use
nginx as a HTTP reverse proxy.

### 2.1 Prerequisites
* **[Python](https://www.python.org/)** 2.7 is installed in Ubuntu
* **[pip](https://pip.pypa.io/en/stable/installing/)** is installed

### 2.2 Install application
* Copy project archive to you ubuntu host.
* Install python libraries that application depends 
    Go to project folder, and execute:  
    `pip install -r requirements.txt`
    
### 2.3 Install uWSGI
For Ubuntu:
* Install c header compiler dependency:  
    `apt-get install build-essential python-dev`
* Install uswgi via pip:   
    `pip install uwsgi`
    * Optionally, you can install *uwsgitop* which is used to monitor uwsgi:  
    `pip install uwsgitop`

### 2.4 Run Django application with uwsgi
Go to django-learning directory and execute one of below commands:
* `uwsgi --http :8080 --wsgi-file djangoproject/wsgi.py`
* `uwsgi --http :9090 -w djangoproject.wsgi`
* `uwsgi -s :9090 -w djangoproject.wsgi -M --pidfile /tmp/uwsgi.pid -p 4 -d uwsgi.log` or  
 `uwsgi --socket :9090 -wsgi djangoproject.wsgi --master --pidfile /tmp/uwsgi.pid --processes --daemonize`
  * -M/--master: Manager worker
  * --pidfile: pid file, with it we can easily to stop uwsgi via:  
  `uwsgi --stop /tmp/uwsgi.pid`
  * -p/--processes: Worker process count
  * -d/--daemonize: Daemonize uWSGI
  * -w/--wsgi: Load a wsgi module
* `uwsgi uwsgi.ini` -- start uWSGI via configuration file.

### 2.5 Install nginx  
Refer to [nginx offical guide](http://nginx.org/en/linux_packages.html).
* Download PGP key for nginx repository signature:  
`wget http://nginx.org/keys/nginx_signing.key`  
`apt-key add nginx_signing.key`

* Add repo
Modify `/et/apt/source.list`, add below 2 lines at the end of file:  
   * For Ubuntu 16.04:  
   `deb http://nginx.org/packages/ubuntu/ xenial nginx`  
   `deb-src http://nginx.org/packages/ubuntu/ xenial nginx`
   * For Ubuntu 14.04:  
   `deb http://nginx.org/packages/ubuntu/ trusty nginx`  
   `deb-src http://nginx.org/packages/ubuntu/ trusty nginx`

* Execute following commands:  
   `apt-get update`  
   `apt-get install nginx`
   
### 2.6 Run Django application with *nginx + uwsgi*
* Modify nginx configuration  
  By default, it locates at `/etc/nginx/`, main configuration is `/etc/nginx/nginx.conf`,
  and sub-configuration is `/etc/nginx/conf.d/default.conf`.  
  Open default.conf and modify `location` like:  
  ```
      location / {
        include /etc/nginx/uwsgi_params;
        uwsgi_pass 127.0.0.1:9090;
      }
  ```
  Additionally, modify `server_name` to IP, like `10.128.184.199`, but not `localhost`.

* Start nginx  
  * Start: `nginx`  
  * Shutdown: `nginx -s stop` or `nginx -s quit`  
  * Reloading configuration: `nginx -s reload`

* Start uWSGI  
  Go to django-learning directory and execute:  
  `uwsgi -s :9090 -w djangoproject.wsgi`