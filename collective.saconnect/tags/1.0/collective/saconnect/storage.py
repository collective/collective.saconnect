from persistent.mapping import PersistentMapping
from zope import annotation, component, interface, lifecycleevent
from UserDict import DictMixin

from interfaces import ISQLAlchemyConnectionStrings

ANNKEY = 'collective.saconnect.storage'

class SQLAlchemyConnectionStrings(DictMixin):
    interface.implements(ISQLAlchemyConnectionStrings)
    component.adapts(annotation.interfaces.IAnnotatable)
    
    def __init__(self, context):
        self.context = context
        annotations = annotation.IAnnotations(self.context)
        self._dict = annotations.setdefault(ANNKEY, PersistentMapping())
    
    def __getitem__(self, key):
        return self._dict[key]
    
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Only plain ascii keys are accepted')
        if not isinstance(value, str):
            raise ValueError('Only plain ascii values are accepted')
        self._dict[key] = value
        lifecycleevent.modified(self, key)
    
    def __delitem__(self, key):
        del self._dict[key]
        lifecycleevent.modified(self, key)
    
    def keys(self):
        return self._dict.keys()
