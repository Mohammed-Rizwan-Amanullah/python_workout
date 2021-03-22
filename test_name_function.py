import unittest
from name_function import get_formated_name

class NamestestCase(unittest.TestCase):
    def test_first_last_name(self):
        formated_name = get_formated_name('mohammed','rizwan')
        self.assertEqual(formated_name, "Mohammed Rizwan")

    def test_first_middle_last(self):
        formated_name = get_formated_name(first = 'mohammed',middle = 'rizwan',last = 'Amanullah')
        self.assertEquals(formated_name, "Mohammed Rizwan Amanullah")

if __name__ =='__main__':
    unittest.main()
