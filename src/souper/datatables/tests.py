import unittest
import doctest 
from pprint import pprint
from interlude import interact
from plone.testing import layered
from .testing import SOUPERLAYER

optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE

TESTFILES = [
    ('base.rst', SOUPERLAYER)
]


def test_suite():
    return unittest.TestSuite([
        layered(
            doctest.DocFileSuite(
                file,
                optionflags=optionflags,
                globs={'interact': interact,
                       'pprint': pprint},
                ), layer=layer
        ) for file, layer in TESTFILES
    ])



if __name__ == '__main__':                                   #pragma NO COVERAGE
    unittest.main(defaultTest='test_suite')                  #pragma NO COVERAGE



