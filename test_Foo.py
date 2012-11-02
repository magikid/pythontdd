import unittest

class FooTests(unittest.TestCase):
    def testFoo(self):
        self.assertFalse(0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()