============
Installation
============

At the command line::

    $ easy_install django-registry

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv django-registry
    $ pip install django-registry

If you want to use template tags, add ``djregistry`` to ``INSTALLED_APPS``::

    # settings.py
    INSTALLED_APPS = [
      ..
      "djregistry",
      ..
    ]

