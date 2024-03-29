"""
  >>> from five.grok.ftests.viewlet.simple import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@painting")
  >>> print(browser.contents)
  <html>
  <body>
  <h2>Modern Art</h2>
  <h2>Classic Art</h2>
  </body>
  </html>

"""
from zope.interface import Interface

from five import grok


class Mammoth(grok.Model):
    pass


class Painting(grok.View):
    grok.context(Interface)


painting = grok.PageTemplate("""\
<html>
<body>
<tal:replace tal:replace="structure provider:art" />
<tal:replace tal:replace="structure provider:nothing" />
</body>
</html>
""")


class Art(grok.ViewletManager):
    grok.view(Painting)
    grok.context(Interface)


class Nothing(grok.ViewletManager):
    grok.context(Interface)
    grok.view(Painting)


class Modern(grok.Viewlet):
    grok.context(Interface)
    grok.order(10)
    grok.view(Painting)
    grok.viewletmanager(Art)


modern = grok.PageTemplate("""\
<h2>Modern Art</h2>
""")


class Classic(grok.Viewlet):

    grok.context(Interface)
    grok.order(20)
    grok.view(Painting)
    grok.viewletmanager(Art)


classic = grok.PageTemplate("""\
<h2>Classic Art</h2>
""")
