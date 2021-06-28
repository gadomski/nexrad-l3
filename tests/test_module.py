import unittest

import stactools.nexrad_l3


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.nexrad_l3.__version__)
