"""
  >>> from five.grok.ftests.view.macros import *
  >>> id = getRootFolder()._setObject("manfred", Mammoth(id='manfred'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/manfred/@@painting")
  >>> print(browser.contents)
  <html>
  <body>
  <h1>GROK MACRO!</h1>
  <div>
  GROK SLOT!
  </div>
  </body>
  </html>

If the view has an attribute with the same name as a macro, the macro
shadows the view. XXX This should probably generate a warning at runtime.

  >>> browser.open("http://localhost/manfred/@@grilldish")
  >>> print(browser.contents)
  <html>
  Curry
  </html>

"""
from zope.interface import Interface

from five import grok


class Mammoth(grok.Model):
    pass


class Grilled(grok.View):
    grok.context(Interface)

    def update(self):
        self.spices = "Pepper and salt"


class Painting(grok.View):
    grok.context(Mammoth)


painting = grok.PageTemplate("""\
<html metal:use-macro="context/@@layout/macros/main">
<div metal:fill-slot="slot">
GROK SLOT!
</div>
</html>
""")


class Layout(grok.View):
    grok.context(Mammoth)


layout = grok.PageTemplate("""\
<html metal:define-macro="main">
<body>
<h1>GROK MACRO!</h1>
<div metal:define-slot="slot">
</div>
</body>
</html>""")


class Dancing(grok.View):
    grok.context(Mammoth)


dancing = grok.PageTemplate("""\
<html metal:use-macro="context/@@dancinghall/macros/something">
</html>
""")


class GrillDish(grok.View):
    grok.context(Mammoth)


grilldish = grok.PageTemplate("""
<html metal:use-macro="context/@@grilled/macros/spices">
</html>""")


grilled = grok.PageTemplate("""\
<html metal:define-macro="spices">
Curry
</html>""")
