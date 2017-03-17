# minirest
## Minimalistic REST API server - add API to any your project
### (python+flask)
- Run ./run.py
- Work in debug mode - if any python file was changed, server restarts automatically
- After run prints on console which IP and port it is listening at
- REST API URLs and functions to process - into app/views.py
- Supports authentication with web-tokens
- In app/views.py some calls had made without authentication for example and some with authentication
- Usernames and passwords are into app/views.py
- To see how token authentications works, look into ./test.py
- Try to run ./test.py – it runs server, checks that server is working and returns index html page, will try to authenticate with correct username/password, with incorrect username, with incorrect password and will try to check server work with token
- Examples of config files for Gunicorn and Apache (if you will run this server in production under load)
- Dockerfile to make docker-application

## How to start
* clone project from gitlab.cisco.com:
* rename directory to your project: mv -f minirest your-project-name
* cd into your project directory: cd your-project-name
* install needed Python modules: pip (or pip3) install -r ./requirements.txt
* run your application "./run.py" or "python ./run.py" or "python3 ./run.py"

## How to run in production
### Apache
```
apt-get install libapache2-mod-wsgi
WSGIDaemonProcess minirest user=rv group=rv threads=5
WSGIScriptAlias /minirest /var/www/minirest/minirest.wsgi
<Directory /var/www/flask>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride None
</Directory>
<Directory /var/www/minirest>
      WSGIProcessGroup minirest
      WSGIApplicationGroup %{GLOBAL}
      Order deny,allow
      Allow from all
</Directory>
```

### Gunicorn
```
$ pip3 install gunicorn
Now, run your app with:
$ gunicorn manage:app
Gunicorn uses port 8000 instead of 5000
```

## Docker
### Package application to Docker container
```
cd minirest
docker build -t <your username>/minirest .
docker images
```
### Run docker application
```
docker run -p 8080:5000 -d <your username>/minirest
docker ps
```
You can now connect to your application to port 8080
### Stop docker application
```
docker ps
docker stop <container id>
```
### Prepare your docker app to give somebody
```
docker save -o minirest.tar <your username>/minirest
gzip minirest.tar
```
### Install prepared app to a new docker server
```
gunzip minirest.tar.gz
docker load -i minirest.tar
docker run -p 80:5000 -d <your username>/minirest
```
