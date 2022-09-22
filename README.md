<h1>Flask Boilerplate :: base</h1>

This is a super simple boilerplate for flask

To run the app in wsgi server, you can use : 
<code>gunicorn --config gunicorn-cfg.py "wsgi:create_app()"</code>

or in docker : 
build image :
<code>docker build --tag python-docker .</code>

run image : 
<code>docker run -d -p 8000:5000 python-docker</code>

To Do : nginx as reverse proxy
