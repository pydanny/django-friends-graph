========================
django-friends-graph
========================

.. image:: http://farm4.static.flickr.com/3472/3928843275_d631c73db4.jpg

A way to visualize django-friends relationships using thejit_. Groups of users
are broken up into sections based off the first letter in their username or full name (if so defined). Names are actually hyperlinks to their profiles.

This package works great in Pinax_. 

Dependencies
============

 * django-friends_
 
Installation
============

Pinax Install
~~~~~~~~~~~~~

No pypi package yet but nevertheless getting django-friends-graph up and running inside of your Pinax environment should be pretty straightforward::

    pip install -e git://github.com/pydanny/django-friends-graph.git#egg=django-friends-graph

Then add it to your installed applications in settings.py::

    INSTALLED_APPS = (
        ...
        'friends_graph',
    )
    
Go add a new route for the urls::


    urlpatterns = patterns('',
        ...
        (r'^graph/', include('friends_graph.urls')),
    )
    
You should be able to go to /graph/<my-user-name> and see yourself and all your friends.

Django Installation
~~~~~~~~~~~~~~~~~~~

Not quite as easy as the Pinax installation but it shouldn't be too hard. Until a formal Pypi release is created, you will need to make sure you've installed the git-scm_ distributed version control system (DVCS) before proceeding. Then you just do the same as Pinax be able to use this package::

    pip install -e git://github.com/pydanny/django-friends-graph.git#egg=django-friends-graph

Then add it to your installed applications in settings.py::

    INSTALLED_APPS = (
        ...
        'friends_graph',
    )
    
Go add a new route for the urls::

    urlpatterns = patterns('',
        ...
        (r'^graph/', include('friends_graph.urls')),
    )

You'll need to move the django-friends-graph media files into wherever you store media in your project.    

You should be able to go to /graph/<my-user-name> and see yourself and all your friends.
 
TODO
====

 * 508 view of data
 * Tests
 * Docs
 
.. _thejit: http://thejit.org/
.. _django-friends: http://github.com/jtauber/django-friends
.. _Pinax: http://pinaxproject.com
.. _git-scm: http://www.git-scm.org/