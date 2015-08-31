'''
Created on Aug 23, 2015

@author: JasonCRodriguez
'''
import unittest
from univperformance import bySector as bs
from datahandler import setup_ipeds_datasets as sid

class Test(unittest.TestCase):


    def setUp(self):
        self.inst = sid.SetupIPEDSData()
        self.df = self.inst.get_data()


    def tearDown(self):
        pass


    def test_bySector(self):
        self.obj = bs.bySector(self.df)
        self.target_var = "ftretention_rate"
        
        self.plot_obj = self.obj.plot(self.target_var)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()