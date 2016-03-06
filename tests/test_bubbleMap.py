
'''
Created on Feb 28, 2016

@author: Jason Rodriguez
'''
import unittest

from bubbleMap import Map as mp

class Test(unittest.TestCase):


    def setUp(self):
        self.object = mp.mapper()


    def tearDown(self):
        pass


    def test_create_latlong_df(self):
        self.df = self.object.create_latlong_df(100)
        
        self.assertItemsEqual(set([0,1,2,3,4]), set(self.df["color_val"]))
	
	self.assertItemsEqual(100, length(self.df["color_val"]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_setup_ipeds_datasets']
    unittest.main()
