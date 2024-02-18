Internationalization
====================

http://www.sphinx-doc.org/en/master/usage/advanced/intl.html

$ make getteext
$ sphinx-intl update -l de -o build/locale
# Translate documentation
$ make SHPINXOPTS="-D languge=en" html

Text
----

1. Extract translatable messages into pot files.

.. code-block:: bash

    Strg+Schift+B -> make-gettext

The generated pot files will be placed in the build/gettext directory.

2. Generate po files.

We’ll use the pot files generated in the above step.

.. code-block:: bash

    Strg+Schift+B -> sphinx-intl-update
    
Once completed, the generated po files will be placed in the below directories:

.. code-block:: bash

    ./locale/de/LC_MESSAGES/
    ./locale/en/LC_MESSAGES/

3. Translate po files.


4. Build translated document.

.. code-block:: bash

    Strg+Schift+B -> make-html-en

Images
------

`figure_language_filename <http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-figure_language_filename>`_.

The filename format for language-specific figures. The default value is {root}.{language}{ext}.
It will be expanded to dirname/filename.en.png from .. image:: dirname/filename.png. The available format tokens are:

{root} - the filename, including any path component, without the file extension, e.g. dirname/filename
{path} - the directory path component of the filename, with a trailing slash if non-empty, e.g. dirname/
{basename} - the filename without the directory path or file extension components, e.g. filename
{ext} - the file extension, e.g. .png
{language} - the translation language, e.g. en

For example, setting this to {path}{language}/{basename}{ext} will expand to dirname/en/filename.png instead.


YouTube
-------

`Writing multi-language documentation using Sphinx <https://www.youtube.com/watch?v=Nz8zutA55fI>`_.
