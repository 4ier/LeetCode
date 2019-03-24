import unittest

from integerToRoman import Solution as I2R
from romanToInteger import Solution as R2I


class TestRomanToInteger(unittest.TestCase):
    global i2r 
    i2r = I2R()
    global r2i
    r2i = R2I()

    def test_roman_to_integer_5(self):
        self.assertEquals(5, r2i.romanToInt(i2r.intToRoman(5)))

    def test_roman_to_integer_11(self):
        self.assertEquals(11, r2i.romanToInt(i2r.intToRoman(11)))

    def test_roman_to_integer_8(self):
        self.assertEquals(8, r2i.romanToInt(i2r.intToRoman(8)))

    def test_roman_to_integer_3999(self):
        self.assertEquals(3999, r2i.romanToInt(i2r.intToRoman(3999)))

    def test_roman_to_integer_4999(self):
        self.assertEquals(499, r2i.romanToInt(i2r.intToRoman(499)))

    def test_roman_to_integer_1024(self):
        self.assertEquals(1024, r2i.romanToInt(i2r.intToRoman(1024)))
