# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 11:18:01 2016

@author: Elayne Ruane
"""

# rename file to data_entry_test

import unittest

from application.data_entry import epochtime
from application.data_entry import parseName
#from application.data_entry import 


class Testing(unittest.TestCase):
    def test_epochtime(self):
        x = 'Mon Nov 02 20:32:06 GMT+00:00 2015'
        expected_result = 1446496326
        actual_result = epochtime(x)
        self.assertEqual(expected_result, actual_result)
    
    def test_parseName(self):
        
        
        
        
        
        


    
#    def parseName(x):
#        inst1 = x.find(">")+2
#        inst2 = x.find(">", inst1)
#        
#        building = x[inst1:inst2-1].lower()
#        room = x[inst2+6:]
#        
#        return (building,room)


if __name__ == '__main__':
    unittest.main()