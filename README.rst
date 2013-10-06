Uptime Robot integration for Django
============

Uptime Robot http://uptimerobot.com integration for your Django project. 
There is a Python version (https://github.com/arteria/python-uptimerobot) available containing only the Uptime Robot API 
implementation.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash
	# TODO:
    $ pip install django-uptimerobot

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/arteria.ch/django-uptimerobot.git#egg=uptimerobot

TODO: Describe further installation steps (edit / remove the examples below):

Add ``uptimerobot`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'uptimerobot',
    )

Add the ``uptimerobot`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^uptimerobot/', include('uptimerobot.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load uptimerobot_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate uptimerobot


Usage
-----

Use with Python or in Django:

.. code-block:: python

    >>> from uptimerobot.uptimerobot import UptimeRobot
    >>> up = UptimeRobot(UPTIME_ROBOT_API_KEY)
    >>> up.addMonitor("arteria-webpage", "https://www.arteria.ch/")
    True


Use in Shell: (success if return value is 0, null)

.. code-block:: bash

    cd /path/to/script/
    chmod 755 uptimerobot.py # if necessary
    ./uptimerobot.py monitorFriendlyName=arteria-webpage monitorURL=https://www.arteria.ch/


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-uptimerobot
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
