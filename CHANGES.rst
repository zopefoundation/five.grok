Changelog
=========

4.1 (unreleased)
----------------

- Nothing changed yet.


4.0 (2025-02-15)
----------------

- Drop support for ``pkg_resources`` namespace and replace it with
  PEP 420 native namespace.
  Caution: This change requires to switch all packages in the `five`
  namespace to versions using a PEP 420 namespace.

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


3.0 (2023-06-29)
----------------

- Drop support for Python 2.7, 3.5, 3.6.


2.0 (2023-03-15)
----------------

- Pin ``five.localsitemanager>=2.0``.  Avoids problems with newer
  version comparison in ``setuptools 8.0``.
  [maurits]

- Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.

- Add support for Zope >= 4.

- Drop support for Zope 2.13.


1.3.2 (2012-08-17)
------------------

- Add an optional support for ``grokcore.layout``, with the extra
  ``layout``.

1.3.1 (2012-05-02)
------------------

- Make formlib support optional. This is not included by default. If
  you whish to use formlib, you need to include the extra ``form`` for
  ``five.grok``. Example:  ``five.grok [form] >= 1.3.1``.

- Fix the redirect method to properly work. Unlike in Zope 3, it
  doesn't support trusted.

1.3.0 (2011-11-07)
------------------

- Clean up code, update dependencies and tests, this release only
  works with Zope 2.13.  [thefunny42]


1.2.0 (2011-01-22)
------------------

- Require five.formlib for Zope 2.13 compatibility. This requires Zope 2.12.3
  or later.
  [elro]

1.1.2 (2010-08-04)
------------------

- Fixed problem with unrestrictedTraverse() and files in subfolders of grokked
  resource directories. This fix also depends on fixes in Zope 2.12.6 or
  later.
  [optilude]

1.1.1 (2010-02-04)
------------------

- Fix namespace override in ZopeTwoPageTemplate, i.e. let users
  override 'view' for instance using the namespace method of a Grok
  view class. This bug was introduced in the 1.1 release.
  [thefunny42]


1.1 (2009-11-16)
----------------

- Update code and tests to work with Zope 2.12. People using Zope 2.10
  and 2.11 should keep using five.grok 1.0.
  [thefunny42 and optilude]

- Update to martian 0.11.1, `grokcore.annotation`_ 1.1 and
  `grokcore.site`_ 1.1, `grokcore.view`_ to 1.12.2.
  [vincentfretin]

- Local utility implements IAttributeAnnotatable, IContext like in
  `grokcore.site`_.
  [thefunny42]


1.0 (2009-09-17)
----------------

- Define an IFiveGrokAPI.
  [thefunny42]

- Fix the broken ``url`` method on views.
  [thefunny42]

- Reverted the CodeView base class, see grokcore.view changelog for
  more details.
  ``CodeView`` is still available as a backwards compatibility alias
  for ``View``. Please update all references to ``CodeView`` to
  ``View``.
  [vincentfretin]


1.0b2 (2009-07-21)
------------------

- Added dependency on grokcore.view 1.9, grokcore.viewlet 1.1 and
  grokcore.formlib 1.2, and support for the new CodeView from grokcore.View.
  [optilude]


1.0b1 (2009-06-30)
------------------

- Added support for annotations with `grokcore.annotation`_.
  [thefunny42]

- Added support for local site and utilities with `grokcore.site`_.
  [thefunny42]

- Fix grok.EditForm when used with grokcore.formlib 1.1.
  The Apply action was gone.
  [thefunny42]

- Let static resource directories allow access to unprotected subattributes
  to avoid authorisation problems when accessing them from protected code.
  [optilude]

- Do not create static resource directories if the 'static' directory does
  not actually exist.
  [optilude]


1.0a2 (2008-11-23)
------------------

- Added support for viewlets with `grokcore.viewlet`_.
  [thefunny42]

- Added support for the DirectoryResource component (new in
  `grokcore.view`_ 1.2).
  [thefunny42]

- Added support for using Zope 2 templates by default when doing ``from
  five import grok`` and using grok.PageTemplateFile (being consistent
  with grok.PageTemplate).
  [thefunny42]

- Added a convenient grok.Container.
  [thefunny42]

- Fix AutoFields (and form grokker) not to include OFS Zope 2 defined
  fields by default. This use to add a lot of buggy and wanted
  fields.
  [thefunny42]


1.0a1 (2008-10-22)
------------------

- Added support for formlib forms with `grokcore.formlib`_.
  [thefunny42]

- Added support for static resource directory.
  [thefunny42]

- Added support for inline templates and made Zope 2 template semantics
  the default when doing ``from five import grok`` and using
  grok.PageTemplate.
  [optilude]

- Added override to make templates use Five's ViewPageTemplateFile instead
  of the one from zope.app.pagetemplate.
  [optilude]

- Added `grokcore.view`_ support with tests.
  [regebro, jfroche, gotcha et al.]

- Added tests for grok.subscriber directive.
  [kamon]

- Initial release (tests for adapters and utilities, initial support for
  views).
  [regebro, gotcha]

.. _grokcore.annotation: http://pypi.python.org/pypi/grokcore.annotation
.. _grokcore.site: http://pypi.python.org/pypi/grokcore.site
.. _grokcore.view: http://pypi.python.org/pypi/grokcore.view
.. _grokcore.viewlet: http://pypi.python.org/pypi/grokcore.viewlet
.. _grokcore.formlib: http://pypi.python.org/pypi/grokcore.formlib
