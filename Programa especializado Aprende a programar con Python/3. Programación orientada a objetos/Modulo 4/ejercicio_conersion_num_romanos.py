import unittest

class RomanNumber(object):
    def int_to_roman(self, n):
        roman_number = ''
        if n == 4:
            roman_number = 'IV'
        else:
            for x in range(n):
                roman_number += 'I'
            return roman_number
    

class RomanNumerTest(unittest.TestCase):
    def setUp(self):
        self.roman_number = RomanNumber()

    def test_one_to_roman(self):
        roman_number = self.roman_number.int_to_roman(1)
        self.assertEqual('I', roman_number)

    def test_two_to_roman(self):
        roman_number = self.roman_number.int_to_roman(2)
        self.assertEqual('II', roman_number)

    def test_three_to_roman(self):
        roman_number = self.roman_number.int_to_roman(3)
        self.assertEqual('III', roman_number)

    def test_four_to_roman(self):
        roman_number = self.roman_number.int_to_roman(4)
        self.assertEqual('IV', roman_number)
    
if __name__ == '__main__':
    unittest.main()