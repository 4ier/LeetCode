import unittest

from regularExpressionMatching import Solution as ems


class TestRegularExpressionMatching(unittest.TestCase):
    global sln
    sln = ems()
    
    def test_matching(self):
        self.assertEqual(True, sln.isMatch('abc', '*'))

    def test_matching_char(self):
        self.assertEqual(False, sln.isMatch('abc', 'ab'))

    def test_matching_dot(self):
        self.assertEqual(True, sln.isMatch('abc', 'ab.'))

    def test_matching_dot1(self):
        self.assertEqual(True, sln.isMatch('aab', 'c*a*b'))

    def test_matching_char(self):
        self.assertEqual(False, sln.isMatch('aa', 'a'))
