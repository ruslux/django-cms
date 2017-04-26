This branch consists of:


``divio/release/3.4.x``

and merged in:
* ``czpython/fixes/3.4.x/5902``
* ``czpython/feature/menu-speed-enhancements``
* ``czpython/fixes/3.4.x/5900``
* ``czpython/fixes/3.4.x/publish-performance``


Then:

```
gulp icons && gulp sass && gulp bundle
python setup.py sdist
devpi login divio
devpi use django-cms/pre-release
devpi upload dist/django-cms-3.4.3.post1.dev10.tar.gz
```
