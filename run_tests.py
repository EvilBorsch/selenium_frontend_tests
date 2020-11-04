# -*- coding: utf-8 -*-
import sys
import unittest

from casses import IdMainPageAndPersonalDataTests
from casses.FoldersTestFirst import FoldersTest

if __name__ == '__main__':
    suites = unittest.TestSuite(
        (
            unittest.makeSuite(FoldersTest),
            unittest.makeSuite(IdMainPageAndPersonalDataTests),
        )
    )
    result = unittest.TextTestRunner().run(suites)
    sys.exit(not result.wasSuccessful())
