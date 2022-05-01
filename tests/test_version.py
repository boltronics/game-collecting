import unittest

import game_collecting


class VersionTestCase(unittest.TestCase):
    """Version tests"""

    def test_version(self):
        """check game_collecting exposes a version attribute"""
        self.assertTrue(hasattr(game_collecting, "__version__"))
        self.assertIsInstance(game_collecting.__version__, str)


if __name__ == "__main__":
    unittest.main()
