import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print 'set up'

    def tearDown(self):
        print 'tear down'

    @classmethod
    def setUpClass(self):
        print 'set up class'

    @classmethod
    def tearDownClass(self):
        print 'tear down class'

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_inupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity = 2).run(suit)