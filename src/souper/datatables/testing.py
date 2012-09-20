from plone.testing import Layer
from node.ext.zodb import OOBTNode
from zope.interface import implementer
from zope.interface import Interface
from zope.component import provideAdapter 
from souper.interfaces import IStorageLocator
from souper.soup import SoupData
from plone.testing import zca


@implementer(IStorageLocator)
class TestStorageLocator(object):
    def __init__(self, context):
        self.context = context

    def storage(self, soup_name):
        if soup_name not in self.context.attrs:
            self.context.attrs[soup_name] = SoupData()
        return self.context.attrs[soup_name]


class SouperTestLayer(Layer):
    def setUp(self):
        zca.pushGlobalRegistry()
        provideAdapter(TestStorageLocator, adapts=[Interface])

    def tearDown(self):
        zca.popGlobalRegistry()

    def testSetUp(self):
        self['storage'] = OOBTNode()

    def testTearDown(self):
        del self['storage']

SOUPERLAYER = SouperTestLayer()
