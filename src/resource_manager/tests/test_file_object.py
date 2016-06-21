import traceback
import unittest

from resource_manager import FileObject


class TestPyPiPackage(unittest.TestCase):
    def test_create_remove(self):
        try:
            fo = FileObject("test", temporary=True)
            fo.remove()
            fo.create()
        except Exception as exc:
            traceback.print_exc()
            self.fail(exc)

if __name__ == "__main__":
    unittest.main()
