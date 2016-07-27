import unittest
import pandas as pd

import calendar
import time

from application.model_functions import *

class Testing(unittest.TestCase):

    def test_isempty(self):
        df1 = pd.DataFrame()
        self.assertTrue(isempty_df(df1))
        df2 = pd.DataFrame([[0,'abcd',0,1,123]],columns=['a','b','c','d','e'])
        self.assertFalse(isempty_df(df2))

    def test_convert_to_epoch(self):

        df1 = pd.DataFrame([["Wednesday, 27-Jul-16 11:37:51 UTC"]],columns=['time'])
        df1 = convert_to_epoch(df1, "time")
        df2 = pd.DataFrame([[1469619471]],columns=['time'])
        self.assertEqual(df1['time'][0], df2['time'][0])

    def room_number(self):
        pass

    def estimate_occ(self):
        pass

    def dataframe_epochtime_to_datetime(self):
        pass


if __name__ == '__main__':
    unittest.main()