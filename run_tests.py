# -*- coding: utf-8 -*-
import sys
import unittest

from casses import IdMainPageAndPersonalDataTests

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(IdMainPageAndPersonalDataTests)
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
