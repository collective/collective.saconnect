from zope.interface.common import mapping
from z3c.saconfig.interfaces import IEngineFactory, ISiteScopedSession

class ISQLAlchemyConnectionStrings(mapping.IMapping):
    """A collection of SQLAlchemy connection strings"""

class ISiteScopedSessionEngineFactory(ISiteScopedSession, IEngineFactory):
    """All in one z3c.saconfig utility"""
