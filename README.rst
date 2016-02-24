===============
django-registry
===============

Provides a registry to stores all sorts of values. Useful for making extensible apps.

Don't hard-code your constants, allow others to redefine them!

Example
=======

Suppose you've found (or made) a blog app that utilizes ``django-registry``.
The code for this app would look something like::

    # models.py
    from djregistry import registry


    class Blog(models.Model):

        def get_archive_url(self):
            return reverse(registry.get("blog.archive.view_name", "blog:archive"), kwargs={"pk" self.pk})


    # blog-menu.html
    {% load i18 %}
    {% load registry %}
    <ul>
      <li><a href="{{ blog.get_archive_url }}">{% trans "blog.archive.title"|from_registry|default:"Archive" %}</a></li>
    </ul>

Let's say you want to use this app in your project, but you'd like to change "Archive" title to something
like "All Posts by Date". And you want to make your custom view to display the archive.
Now you can totally do that! Just add ``REGISTRY`` to your ``settings.py`` and fill it with some values::

    # settings.py
    REGISTRY = {
      {
        "blog": {
          {"archive": {
            {
              "title": "All Posts by Date",
              "view_name": "mycustomblog:allposts",
            }
          }
        },
      }
    }

