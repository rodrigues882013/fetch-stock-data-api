import json
import unittest

from fetch_stock_data_api.stock.service import StockService


class AppTest(unittest.TestCase):

    def test_if_fetch_data_exist(self):
        self.assertTrue(hasattr(StockService, 'fetch_data'))

if __name__ == '__main__':
    unittest.main()
