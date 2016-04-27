from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget


grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):
    
    button_description = schema.TextLine(
            title = u"Add File Portlet Button Label",
            required=False,
        )


class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    
    def __init__(self, button_description=None):
        self.button_description = button_description
       
       
    @property
    def title(self):
        return "Add File Portlet"
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('templates/addevaldocportlet.pt')
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
        
    def contents(self):
        return self.data

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add 'Add File Portlet'"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit 'Add File Portlet'"
    description = ''
