import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorret default size')

    def test_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')
def suit():
    suit = unittest.TestSuit()
    suit.addTest(WidgetTestCase('test_default_size'))
    suit.addTest(WidgetTestCase('test_resize'))
    return suit

def suit_map()
    tests = ['test_default_size', 'test_resize']
    return unittest.TestSuit(map(WidgetTestCase, tests))

def funtest()
    # testcase = unittest.FunctionTestCase(testSomething)
    pass

if __name__ == '__main__':
    defaultSizeTestCase = WidgetTestCase('test_default_size')
    resizeTestCase = WidgetTestCase('test_resize')

