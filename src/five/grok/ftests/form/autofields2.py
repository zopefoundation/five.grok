"""
  >>> from five.grok.ftests.form.autofields2 import *
  >>> id = getRootFolder()._setObject("montparnasse", House(id='montparnasse'))

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False

  We can test the display form as default view:

  >>> browser.open("http://localhost/montparnasse")
  >>> print(browser.contents)
  <html>...
  ... Name of the building ...
  ... Number of floors ...
  </html>

  But we have an edition form:

  >>> browser.open("http://localhost/montparnasse/edit")
  >>> browser.getControl('Name of the building').value = 'Tour Montparnasse'
  >>> browser.getControl('Number of floors').value = '56'
  >>> browser.getControl('Apply').click()
  >>> 'Updated' in browser.contents
  True

  And if we look back to the display form, we will see new values:

  >>> browser.open("http://localhost/montparnasse")
  >>> print(browser.contents)
  <html>...
  ... Name of the building ...
  ... Tour Montparnasse ...
  ... Number of floors ...
  ... 56 ...
  </html>

"""

from zope import interface
from zope import schema
from zope.schema.fieldproperty import FieldProperty

from five import grok


class IHouse(interface.Interface):

    name = schema.TextLine(title="Name of the building")
    height = schema.Int(title="Number of floors")


@grok.implementer(IHouse)
class House(grok.Container):

    name = FieldProperty(IHouse['name'])
    height = FieldProperty(IHouse['height'])


class Edit(grok.EditForm):
    grok.context(House)

    form_fields = grok.AutoFields(House)


class Index(grok.DisplayForm):
    grok.context(House)
