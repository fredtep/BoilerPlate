<h1>Flask Boilerplate :: base</h1>

This is a super simple boilerplate for flask

To run the app in wsgi server, you can use : 
<code>gunicorn --config gunicorn-cfg.py "wsgi:create_app()"</code>

or in docker : 
<code>docker-compose -f docker-compose.dev.yml up --build -d</code>
