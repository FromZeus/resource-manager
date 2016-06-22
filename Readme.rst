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
  ``ResourceManager.__init__(self, base_path="/some/base", mode=0o744, temporary=True, rand_prefix=True)``
    ``...``

Or you can just use it as an object

``from resource_manager import ResourceManager``

``...``

``with ResourceManager(base_path="/some/base", mode=0o744, temporary=True, rand_prefix=True) as rm:``
  ``rm.mkdir("alias", "path", "mode", "is_temporary")``

  ``rm.cd("path")``

  ``rm.mkfile("alias", "file_name", "is_temporary")``

  ``rm.ls()``

  ``rm.back()``

  ``rm.ls()``

  ``rm.rm("alias")``

There is much more inside :)