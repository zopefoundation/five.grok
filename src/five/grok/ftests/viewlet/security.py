"""
  >>> from five.grok.ftests.viewlet.security import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Products.Five.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@painting")
  >>> print browser.contents
  <html>
  <body>
  <p>A common gallery with rembrandt</p>
  </body>
  </html>

"""
from five import grok

class Mammoth(grok.Model):
    pass

class Painting(grok.View):
    pass

painting = grok.PageTemplate("""\
<html>
<body>
<tal:replace tal:replace="structure provider:museum" />
</body>
</html>
""")

class Museum(grok.ViewletManager):

    grok.view(Painting)


class Gallery(grok.Viewlet):

    grok.view(Painting)
    grok.viewletmanager(Museum)

    def render(self):
        return u'<p>A common gallery with rembrandt</p>'

class Reserve(grok.Viewlet):

    grok.view(Painting)
    grok.viewletmanager(Museum)
    grok.require('zope2.ViewManagementScreens')

    def render(self):
        return u'<p>Non exposed content</p>'
