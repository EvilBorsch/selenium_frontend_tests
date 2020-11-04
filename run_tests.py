# -*- coding: utf-8 -*-
import sys
import unittest

from casses import IdMainPageAndPersonalDataTests
from casses.ContactsCase import ContactsTest
from casses.FoldersTestFirst import FoldersTest
from casses.FoldersTestSecond import FoldersTestSecond
from casses.PasswordCase import PasswordTest
from casses.SecurityCase import SecurityTest

if __name__ == '__main__':
    suites = unittest.TestSuite(
        (
            unittest.makeSuite(PasswordTest),
            unittest.makeSuite(ContactsTest),
            unittest.makeSuite(SecurityTest),
            unittest.makeSuite(FoldersTest),
            unittest.makeSuite(FoldersTestSecond),
            unittest.makeSuite(IdMainPageAndPersonalDataTests),
        )
    )
    result = unittest.TextTestRunner().run(suites)
    sys.exit(not result.wasSuccessful())
