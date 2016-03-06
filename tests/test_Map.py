'''
Created on Aug 30, 2015

@author: J4ROD2
'''
import unittest
from bubbleMap import Map as mp

class Test(unittest.TestCase):


    def setUp(self):
        self.object = mp.Mapper()
        pass

    def tearDown(self):
        pass


    def test_get_universities(self):

        import os
        self.path = os.path.join(os.getcwd(), 'data/GeolocData.csv')

        try:
            self.df = self.object.get_universities(self.path)

        except:
            print "doesn't like this path %s" % self.path

        print self.df


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_setup_ipeds_datasets']
    unittest.main()
