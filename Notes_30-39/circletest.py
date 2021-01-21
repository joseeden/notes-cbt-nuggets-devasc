#*******************************************************
# circletest.py
#
# This is the code used in '33-Unit_Tests_TDD.md'.
# Calculates circumference of a circle, given the 
# raius(r)
#*******************************************************

import math
import unittest

# this is the function that we'll test
# This computes circumference fo a circle, given the radius (r)
def circum(r):
    return 2*math.pi*r

# Test Cases
class testcircle(unittest.TestCase):
    
    # Test Case 1
    def testcircum_valid(self):
        # if cirucm(5) is equal to value after it,
        # it will return OK
        self.assertEqual(circum(5),31.41592653589793)

    # Test Case 2
    def testcircum_zero(self):
        self.assertEqual(circum(0),0)

    # Test Case 3
    # def testcircum_text(self):
    #    self.assertRaises(circum("Frank"))

# calls the testcase
unittest.main()

