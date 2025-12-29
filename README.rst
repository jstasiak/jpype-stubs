================
jpype-java-stubs
================

The `JPype <https://jpype.readthedocs.io/en/latest/index.html>`_ ``java.*`` type definitions.
They cover imports like ``from java.util import ArrayList``.

There are two mutually exclusive variants distributed under different names:

1. ``java-stubs`` (no automated Java string to Python string conversions)
2. ``java-stubs-converted-strings`` (with the conversions)

Some details from `JPype string conversions documentation
<https://jpype.readthedocs.io/en/latest/userguide.html#string-conversions>`_:

    The ``convertStrings`` argument controls whether Java strings are automatically
    converted to Python strings. By default, this behavior is disabled
    (``convertStrings=False``) to preserve Java string methods and avoid unnecessary conversions.

    If enabled (``convertStrings=True``), Java strings are returned as Python strings, but this
    can impact performance and chaining of Java string methods. This option is consisted a legacy
    option as it will result in unncessary calls to str() every time a String is passed from Java.

    Best practice: Set ``convertStrings=False`` unless your application explicitly requires
    automatic conversion.

Which version you need depends on the ``convertStrings`` value used when starting the JVM.

Both of these distributions provide the ``java-stubs`` package providing type definitions
for the whole ``java.*`` namespace.

The stubs are produced with `CERN's stubgenj <https://gitlab.cern.ch/scripting-tools/stubgenj>`_.

There's a related `JPype discussion <https://github.com/jpype-project/jpype/issues/714>`_.

Known limitations
-----------------

* The types are tied to a specific Java version (currently OpenJDK 25).
* The JPype version used when generating the types may affect them, currently
  only one version is used.
* A few Java -> Python ``stubgenj`` translation problems have been reported, some are
  very difficult to resolve in a way that will satisfy all users (more:
  https://gitlab.cern.ch/scripting-tools/stubgenj/-/issues).

Internal documentation
----------------------

Run ``./generate`` to regenerate the stubs.
