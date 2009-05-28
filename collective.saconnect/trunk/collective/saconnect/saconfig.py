# optional z3c.saconfig support
from zope.component import getUtility
from zope.component import getSiteManager
from z3c.saconfig.interfaces import IEngineFactory, ISiteScopedSession
from z3c.saconfig.utility import EngineFactory
from z3c.saconfig.utility import SiteScopedSession
from z3c.saconfig.utility import SESSION_DEFAULTS
from Products.CMFCore.interfaces import ISiteRoot
from persistent import Persistent

from interfaces import ISQLAlchemyConnectionStrings


class ISiteScopedSessionEngineFactory(ISiteScopedSession, IEngineFactory):
    """All in one z3c.saconfig utility"""


class SiteScopedSessionEngineFactory(SiteScopedSession, EngineFactory,
                                     Persistent):
    """An all in one z3c.saconfig utility
    TODO: add configuration options
    """

    def __init__(self, name):
        self.name = name

    @property
    def _key(self):
        siteroot = getUtility(ISiteRoot)
        return "collective.saconnect:%s,%s" % (self.name, siteroot._p_oid)

    def configuration(self):
        siteroot = getUtility(ISiteRoot)
        connections = ISQLAlchemyConnectionStrings(siteroot)
        url = connections[self.name]
        return [url], dict(convert_unicode=True)

    # SiteScopedSession

    @property
    def engine(self):
        return self.name

    @property
    def kw(self):
        return SESSION_DEFAULTS

    def siteScopeFunc(self):
        return id(getSiteManager())


def syncUtility(connections, event):
    """Subscriber
    """
    sm = getSiteManager()
    for key in event.descriptions:
        factory = sm.queryUtility(ISiteScopedSessionEngineFactory, name=key)
        if key in connections.keys():
            if factory is not None:
                factory.reset() # modify
            else:
                factory = SiteScopedSessionEngineFactory(key)
                sm.registerUtility(factory, name=key,
                    provided=ISiteScopedSessionEngineFactory) # add
        else:
            if factory is not None:
                factory.reset()
                sm.unregisterUtility(factory, name=key,
                    provided=ISiteScopedSessionEngineFactory) # delete
