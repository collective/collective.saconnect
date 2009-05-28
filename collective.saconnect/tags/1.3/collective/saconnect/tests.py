import unittest
from zope.component import provideAdapter
from zope.interface import directlyProvides
from zope.testing import cleanup
from collective.saconnect.interfaces import ISQLAlchemyConnectionStrings
from Products.GenericSetup.testing import BodyAdapterTestCase
from UserDict import UserDict

class SAConnectionStringsImportExportTests(BodyAdapterTestCase):
    _BODY = '''\
<?xml version="1.0"?>
<connections>
 <connection name="bar" string="eggs"/>
 <connection name="foo" string="spam"/>
</connections>
'''
    
    def setUp(self):
        self._obj = UserDict()
        directlyProvides(self._obj, ISQLAlchemyConnectionStrings)
        provideAdapter(self._getTargetClass())
    
    def tearDown(self):
        cleanup.cleanUp()
        
    def _getTargetClass(self):
        from collective.saconnect.genericsetup import \
            SQLAlchemyConnectionStringsXMLAdapter
        return SQLAlchemyConnectionStringsXMLAdapter
    
    def _populate(self, obj):
        obj['foo'] = 'spam'
        obj['bar'] = 'eggs'
    
    def _verifyImport(self, obj):
        self.assertEqual(obj, dict(foo='spam', bar='eggs'))

del BodyAdapterTestCase

def test_suite():
    import sys
    return unittest.findTestCases(sys.modules[__name__])
