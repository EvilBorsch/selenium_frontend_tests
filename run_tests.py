# -*- coding: utf-8 -*-
import sys
import unittest
from casses import FoldersUpdateTest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FoldersUpdateTest())
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
