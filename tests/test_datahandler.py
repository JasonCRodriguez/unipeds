'''
Created on Aug 30, 2015

@author: J4ROD2
'''
import unittest
from datahandler import setup_ipeds_datasets as sid

class Test(unittest.TestCase):


    def setUp(self):
        self.object = sid.SetupIPEDSData()


    def tearDown(self):
        pass


    def test_setup_ipeds_datasets(self):
        self.df = self.object.get_data()
        
        self.assertItemsEqual(set(['1','2','3']), set(self.df["sector"]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_setup_ipeds_datasets']
    unittest.main()
