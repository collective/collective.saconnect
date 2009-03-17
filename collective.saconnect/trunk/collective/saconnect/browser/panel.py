from plone.z3cform.crud import crud
from plone.app.z3cform.layout import wrap_form
from zope import component, interface, schema
from zope.i18n import translate
from Products.CMFCore.interfaces import ISiteRoot

from collective.saconnect import MessageFactory as _
from collective.saconnect.interfaces import ISQLAlchemyConnectionStrings

#
# One row in the form
# 
class IConnectionLine(interface.Interface):
    connname = schema.ASCIILine(
        title=_(u'label_connection_name', default=u'Connection name'),
        description=_(u'description_connection_name', default=u''),
        required=True,
    )
    connstring = schema.ASCIILine(
        title=_(u"label_connection_string",
            default=u"SQLAlchemy connection string"),
        description=_(u"description_connection_string",
            default=u"driver://user:password@hostname/database"),
        required=True,
        default="sqlite:///"
    )

class ConnectionLine(object):
    interface.implements(IConnectionLine)
    connname = None
    connstring = None
    def __init__(self, name, string):
        self.connname = name
        self.connstring = string

class SQLAlchemyConnectionsForm(crud.CrudForm):
    label = _(u'label_saconnectform', u'Manage SQLAlchemy connection strings')
    update_schema = IConnectionLine
    
    def __init__(self, context, request):
        crud.CrudForm.__init__(self, context, request)
        self.storage = ISQLAlchemyConnectionStrings(
            component.getUtility(ISiteRoot))
    
    def get_items(self):
        names = self.storage.keys()
        names.sort()
        return [(name, ConnectionLine(name, self.storage[name]))
            for name in names]
    
    def add(self, data):
        name = data['connname'].strip()
        if str(name) in self.storage:
            msg = _(u'error_name_already_registered',
                u'The connection name is already registered')
            msg = translate(msg, self.request)
            raise schema.ValidationError(msg)
        
        self.storage[name] = data['connstring'].strip()
        return ConnectionLine(name, data['connstring'].strip())

    def remove(self, (id, item)):
        del self.storage[item.connname]

SQLAlchemyConnectionsView = wrap_form(SQLAlchemyConnectionsForm)
