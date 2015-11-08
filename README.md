Learning-Flask-API
------------------

Building an API scoffold piece by piece to learn the best way to set this up.

Starting with Flask-JWT.  min-app.py is straight from the Flask-JWT docs.

to get a token, POST to localhost:5000/auth with user credentials:

    $http POST localhost:5000/auth username="user1" password="abcxyz"
    HTTP/1.0 200 OK
    Content-Length: 192
    Content-Type: application/json
    Date: Sat, 24 Oct 2015 18:18:53 GMT
    Server: Werkzeug/0.10.4 Python/3.5.0

    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0NDU3MTA5MTAsIm5iZiI6MTQ0NTcxMDkxMCwiaWRlbnRpdHkiOjEsImV4cCI6MTQ0NTcxMTIxMH0.awUrJdUHIioL2w-IiE-rx7E2lP5-XjZpLcvvdvl3HFM"
    }

then to use the token, GET whatever protected resource you need:

    $http GET localhost:5000/protected Authorization:'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0NDU3MTA5MTAsIm5iZiI6MTQ0NTcxMDkxMCwiaWRlbnRpdHkiOjEsImV4cCI6MTQ0NTcxMTIxMH0.awUrJdUHIioL2w-IiE-rx7E2lP5-XjZpLcvvdvl3HFM'
    HTTP/1.0 200 OK
    Content-Length: 12
    Content-Type: text/html; charset=utf-8
    Date: Sat, 24 Oct 2015 18:23:03 GMT
    Server: Werkzeug/0.10.4 Python/3.5.0

    User(id='1')

To initialize and migrate the DB:

    python server.py db init
    python server.py db migrate
    python server.py db upgrade

To see the URL endpoints:

    python server.py urls

To run the development server:

    python server.py runserver
