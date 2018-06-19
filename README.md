# Flask Sample Application

*Giving credit where credit is due, this project has been forked from [https://github.com/OpenShiftDemos/os-sample-python](https://github.com/OpenShiftDemos/os-sample-python). 
You can find other fantastic OpenShift demo projects at [https://github.com/OpenShiftDemos](https://github.com/OpenShiftDemos).*

This repository provides a sample Python web application implemented using the Flask web framework and hosted using 
``gunicorn``. It is intended to be used to demonstrate deployment of Python web applications to OpenShift 3.

## Implementation Notes

This sample Python application relies on the support provided by the default S2I builder for deploying a WSGI 
application using the ``gunicorn`` WSGI server. The requirements which need to be satisfied for this to work are:

* The WSGI application code file needs to be named ``wsgi.py``.
* The WSGI application entry point within the code file needs to be named ``application``.
* The ``gunicorn`` package must be listed in the ``requirements.txt`` file for ``pip``.

In addition, the ``.s2i/environment`` file has been created to allow environment variables to be set to override the 
behaviour of the default S2I builder for Python.

* The environment variable ``APP_CONFIG`` has been set to declare the name of the config file for ``gunicorn``.

## Deployment Steps

To deploy this sample Python web application from the OpenShift web console, you should select ``python:2.7``, 
``python:3.3``, ``python:3.4`` or ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same 
as having selected the most up to date Python version available, which at this time is ``python:3.4``.

The HTTPS URL of this code repository which should be supplied to the _Git Repository URL_ field when using _Add to 
project_ is:

* https://github.com/kovarus/os-sample-python-flask.git

If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web 
application, you can run:

```
oc new-app https://github.com/kovarus/os-sample-python-flask.git
```

In this case, because no language type was specified, OpenShift will determine the language by inspecting the code 
repository. Because the code repository contains a ``requirements.txt``, it will subsequently be interpreted as 
including a Python application. When such automatic detection is used, ``python:latest`` will be used.

If needing to select a specific Python version when using ``oc new-app``, you should instead use the form:

```
oc new-app python:2.7~https://github.com/kovarus/os-sample-python-flask.git
```
To create a route to access the application, run the command:

```
oc expose service os-sample-python-flask
```

and get the route/url to access the app, type the command:

```
 oc get route
```

output:

```
NAME                    HOST/PORT                                               PATH       SERVICES                 PORT      TERMINATION   WILDCARD

os-sample-python-flask   os-sample-python-flask-python.192.168.99.100.nip.io               os-sample-python-flask   8080-tcp                 None
```

and point your browser to `http://os-sample-python-flask-python.<ip address>.nip.io`

From here you can fork and edit as you please!


You can find a great Flask tutorial for beginners [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)




 
