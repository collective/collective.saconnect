Introduction
============

This package provides a simple control panel and storage for SQLAlchemy
connection strings. It presents a form where one can add and remove named
connections, and a GS import and export step to manage these.

This package does *not* provide SQLAlchemy integration itself; use a
library like zope.sqlalchemy or collective.lead instead.

Example usage::

    from zope.app.component.hooks import getSite
    from collective.saconnect.interfaces import ISQLAlchemyConnectionStrings
    
    saconnect = ISQLAlchemyConnectionStrings(getSite())
    myconnection = saconnect['myidentifier']

ISQLAlchemyConnectionStrings acts as a simple dictionary, although it's keys 
and values must be simple strings.

To import connection strings through GenericSetup, simply include a file named
saconnections.xml in your profile, with a top-level 'connections' element and
one 'connection' element per connection, with name and string attributes::

    <?xml version="1.0"?>
    <connections>
     <connection name="bar" string="sqlite:////path/to/bar.sqlite"/>
     <connection name="foo" string="oracle://username:password/tnsnamethere"/>
    </connections>

To remove any of the connections, use the 'remove' attribute::

    <?xml version="1.0"?>
    <connections>
      <connection name="bar" remove=""/>
    </connections>

If you cache your SQLAlchemy connections, you may want to listen for the
IObjectModifiedEvent for ISQLAlchemyConnectionStrings; the event includes
the key of the modified string, so you can easily refresh your database
connections::

    <subscriber 
        handler=".mymodule.saconnectionUpdated"
        for="collective.saconnect.interfaces.ISQLAlchemyConnectionStrings
             zope.lifecycleevent.interfaces.IObjectModifiedEvent"
        />
    def saconnectionUpdated(connections, event):
        if 'myconnectionstring' in event.descriptions:
            getUtility(IDatabase, u'myconnection').invalidate()


Credits
-------

Development sponsored by
    Elkjøp Nordic AS

Design and development
    `Martijn Pieters`_ at Jarn_

.. _Martijn Pieters: mailto:mj@jarn.com
.. _Jarn: http://www.jarn.com/
