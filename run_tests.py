#!/usr/bin/env python2

import sys
import unittest
from tests.tests import LoginTest
from tests.tests import FoldersTest


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginTest))
    suite.addTest(unittest.makeSuite(FoldersTest))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
