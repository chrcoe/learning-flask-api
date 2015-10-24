# learning-flask-api
learning how to use flask-jwt and flask-restful to create flask-based API (cookiecutter-flask-restful)



Cookiecutter Flask RESTful
==========

This is a basic boilerplate app that can be used with Cookiecutter
to scaffold new flask restful application.

> If you find a bug in project, please open a ticket.


## Installation and Usage
```sh
$ mkdir ~/flaskProjects
$ cd flaskProjects
$ virtualenv venv
$ source venv/bin/activate
(venv) $ cookiecutter gh:xk0nsid/cookiecutter-flask-restful
```

Answer the asked questions properly.

```sh
(venv) $ cd project_name
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py db init
(venv) $ python manage.py db migrate
(venv) $ python manage.py db upgrade
(venv) $ python manage.py runserver
```

## Features

The app comes with some  basic stuff. Like Basic user model. Basic views for
the user etc. Below is the list of avalable endpoints

### Endpoints

|             URI               |     Protected     |    HTTP Method    |             Action
|:---------                     |:--:               |:--:               |--:
| **/version/users/**   | Yes               | GET               | Get list of all users
| **/version/users/**           | No                | POST              | Create a new user
| **/version/users/**           | No                | OPTIONS           | Help for the given endpoint
| **/version/users/user_id**    | Yes               | GET               | Get data of a single user
| **/version/users/user_id**    | No                | OPTIONS           | Help for the given endpoint
| **/auth/**                    | No                | GET               | Request auth token

### Usage of Protected Routes

#### Create a user first

```sh
(venv) $ http POST http://localhost:5000/v1.0/users/ first_name="firstname"
last_name="lastname" username="username" password="password"

# Response should be something like this.
HTTP/1.0 201 CREATED
API-Version: 1.0
Content-Length: 169
Content-Type: application/json
Date: Wed, 29 Jul 2015 06:08:22 GMT
Location: http://localhost:5000/v1.0/users/username
Server: Werkzeug/0.10.4 Python/2.7.6

{
    "first_name": "firstname",
    "id": 1,
    "last_name": "lastname",
    "location": "http://localhost:5000/v1.0/users/username",
    "username": "username"
}
```

#### Get Auth Token for that user
```sh
(venv) $ http POST http://localhost:5000/auth username="username"
password="password"

# Response
HTTP/1.0 200 OK
Content-Length: 146
Content-Type: application/json
Date: Wed, 29 Jul 2015 06:11:17 GMT
Server: Werkzeug/0.10.4 Python/2.7.6

{
    "token": "auth_token"
}
```

#### Access protected routes
```sh
(venv) $ http GET http://localhost:5000/v1.0/users/ "Authorization: Bearer
auth_token"
```
