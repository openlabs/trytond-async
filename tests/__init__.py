# -*- coding: utf-8 -*-
"""
    tests/__init__.py
    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

import trytond.tests.test_tryton

from tests.test_async import TestAsync
from tests.test_serialization import TestSerialization


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestAsync),
        unittest.TestLoader().loadTestsFromTestCase(TestSerialization),
    ])
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
