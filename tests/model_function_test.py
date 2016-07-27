import unittest
import pandas as pd

from application.model_functions import *

class Testing(unittest.TestCase):

    def test_isempty(self):
        df1 = pd.DataFrame()
        self.assertTrue(isempty_df(df1))
        df2 = pd.DataFrame([[0,'abcd',0,1,123]],columns=['a','b','c','d','e'])
        self.assertFalse(isempty_df(df2))

    def test_convert_to_epoch(self):
        self.assertEqual()

    def room_number(self):
        pass

    def estimate_occ(self):
        pass

    def dataframe_epochtime_to_datetime(self):
        pass


if __name__ == '__main__':
    unittest.main()