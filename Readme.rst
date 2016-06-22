===============
ResourceManager
===============

Description
-----------

This module is designed to relief and simplify interaction of your
python modules with the file system.


Installation
------------

python setup.py install


How to use
----------

For example, you can inherit your class from ``ResourceManager`` class

``from resource_manager import ResourceManager``

``...``

``class Foo(ResourceManager, ...):``
  ``ResourceManager.__init__(self, base_path="/some/base", mode=0o644, temporary=True, rand_prefix=True)``
    ``...``

Or you can just use it as an object

``from resource_manager import ResourceManager``

``...``

``rm = ResourceManager(base_path="/some/base", mode=0o644, temporary=True, rand_prefix=True)``
``rm.mkdir("some_alias", "some_path", )``