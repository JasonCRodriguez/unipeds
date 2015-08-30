'''
Created on Aug 23, 2015

@author: JasonCRodriguez
'''
import unittest
import pandas as pd
import numpy as np


class Test(unittest.TestCase):


    def setUp(self):
        self.variable = pd.Series(np.random.random_integers(100,200,size=500))
        pass


    def tearDown(self):
        pass


    def test_bySector(self):
        self.assertAlmostEqual(len(self.variable), 498, msg = "Not long enough: %d ne %d" % (len(self.variable), 498) , delta=1)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()