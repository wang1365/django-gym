# django-learning

## 1. MySQL support
To connect to mysql, Django depends on mysqldb lib provided by *[mysqlclient](https://github.com/PyMySQL/mysqlclient-python)*.

#### How to install mysqlclient:  
* For windows, download wheel from *[Unoffical PYPI](http://www.lfd.uci.edu/~gohlke/pythonlibs)* and install it.  
* For Ubuntu, execute the following commands:  
>> `sudo apt-get install python-dev libmysqlclient-dev`   
`pip install mysqlclient`



## 2. Deployment
We use uwsgi to run the application. For a real productive deployment, we also need to use
nginx as a HTTP reverse proxy.

### 2.1 Install uWSGI
For Ubuntu:
* Install c header compiler dependency: `apt-get install build-essential python-dev`
* Install uswgi via pip: `pip install uwsgi`

### 2.2 Run Django application with uwsgi
Go to django-learning directory and execute one of below commands:
* `uwsgi --http :8080 --wsgi-file djangoproject/wsgi.py`
* `uwsgi --http :9090 -w djangoproject.wsgi`

### 2.3 Install nginx  
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
   
### 2.4 Run Django application with *nginx + uwsgi*
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

* Start uwsgi  
  Go to django-learning directory and execute:  
  `uwsgi -s :9090 -w djangoproject.wsgi`