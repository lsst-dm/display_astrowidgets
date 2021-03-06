import unittest

import lsst.utils.tests
import lsst.display.astrowidgets


class ImportTest(unittest.TestCase):
    def testImport(self):
        self.assertTrue(hasattr(lsst.display.astrowidgets, "Ds9Error"))


class TestMemory(lsst.utils.tests.MemoryTestCase):
    pass


def setup_module(module):
    lsst.utils.tests.init()


if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
