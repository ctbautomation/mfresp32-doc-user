# with overline, for parts
* with overline, for chapters
=, for sections
-, for subsections
^, for subsubsections
“, for paragraphs

#####
parts
#####

********
chapters
********

sections
========

subsections
-----------

subsubsections1
^^^^^^^^^^^^^^^

subsubsections2
***************

subsubsections3
+++++++++++++++

subsubsections4
'''''''''''''''

subsubsections5
...............

subsubsections6
```````````````

subsubsections7
~~~~~~~~~~~~~~~

Paragraph
“““““““““


Code blocks
-----------

.. highlight:: c

.. code-block:: bash

   sudo apt-get update
   sudo apt-get upgrade

.. code-block:: c

   code

.. code-block:: ruby
	
   code
	
.. code-block:: python

   import image


Images
------

Example for image usage:

.. image:: /images/de_schaltzeiten_dialog_button_übernehmen.png
   :width: 200px
   :height: 100px
   :scale: 50 %
   :alt: alternate text
   :align: center

Mit einem Klick auf die Schaltfläche |Übernehmen| werden die Zeiten in der Steuerung übernommen.

.. |Übernehmen| image:: /images/de_schaltzeiten_dialog_button_übernehmen.png
   :scale: 75 %
   
   
Example for figure usage:

.. figure:: picture.png
   :scale: 50 %
   :align: center

	This is the caption of the figure (a simple paragraph).

   
.. figure:: /images/de_anzeigen_historik_auswahl_zeit_anfang.png
   :align: center
   :scale: 100 %
	
   In diesem Bild ist ein Zeitbereich vom „15.02.2002 13:46 Uhr bi zum „03.03.2003 13:49 Uhr“ ausgewählt.

Links
-----

Test hyperlink: `Stack Overflow <http://stackoverflow.com/>`_.

Test hyperlink: SO_.

.. _SO: http://stackoverflow.com/



Raw HTML
--------

.. raw:: html

  <video width="560" height="315" controls>
      <source src="_static/mfresp32_install.mp4" type="video/mp4">
  </video>



Inline markup
-------------

http://www.sphinx-doc.org/en/1.4.9/rest.html#inline-markup

The standard reST inline markup is quite simple: use

one asterisk: *text* for emphasis (italics),
two asterisks: **text** for strong emphasis (boldface), and
backquotes: ``text`` for code samples.


Directives Admonitions:
-----------------------

http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives

Admonitions: attention, caution, danger, error, hint, important, note, tip, warning and the generic admonition. (Most themes style only “note” and “warning” specially.)

.. attention:: attention.

.. caution:: caution.

.. error:: error.

.. hint:: hint.

.. important:: important.

.. note:: note.

.. tip:: tip.

.. warning:: warning.


Tables
------
	
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+
	
	
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======



Line break
----------

| 1. Line
| 2. Line



Roles
-----

.. role:: red

This is :red:`just` a test …

.. role:: black
.. role:: gray
.. role:: grey
.. role:: silver
.. role:: white
.. role:: maroon
.. role:: red
.. role:: magenta
.. role:: fuchsia
.. role:: pink
.. role:: orange
.. role:: yellow
.. role:: lime
.. role:: green
.. role:: olive
.. role:: teal
.. role:: cyan
.. role:: aqua
.. role:: blue
.. role:: navy
.. role:: purple

.. role:: under
.. role:: over
.. role:: blink
.. role:: line
.. role:: strike

.. role:: it
.. role:: ob

.. role:: small
.. role:: large

.. role:: center
.. role:: left
.. role:: right




ToDo
----

.. todo::

   Add text here

todo_include_todos = True in conf.py
   
   
   
Math
----
   
.. math::

   ax^2 + bx + c = 0

   x_1 = \frac{-b+\sqrt{b^2-4ac}}{2a}
   x_2 = \frac{-b-\sqrt{b^2-4ac}}{2a}w
   
   
 
Include
-------

.. include:: telenotgerät_tas_x30_isdn.inc



Kommentar
---------

.. Kommentar
   Kommentar

   
   
   
   
   
:orphan:


.. footer::

  Page ###Page### of ###Total###

| Hatherleigh, Okehampton, Devon
| United Kingdom
|
| email  web@pkimber.net
| mobile 07840 538 357

