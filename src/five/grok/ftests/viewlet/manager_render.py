"""
  >>> from five.grok.ftests.viewlet.manager_render import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@painting")
  >>> print(browser.contents)
  <html>
  <body>
  <p>Art is beautiful</p>
  </body>
  </html>

"""
from five import grok


class Mammoth(grok.Model):
    pass


class Painting(grok.View):
    grok.context(Mammoth)


class Art(grok.ViewletManager):
    grok.context(Mammoth)
    grok.view(Painting)

    def render(self):
        return '<p>Art is beautiful</p>'


painting = grok.PageTemplate("""\
<html>
<body>
<tal:replace tal:replace="structure provider:art" />
</body>
</html>
""")
