import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

    for q in quotes:
      stock = q['stock']
      bid = float(q['top_bid']['price'])
      ask = float(q['top_ask']['price'])
      price = (bid + ask) / 2

      self.assertEqual(getDataPoint(q), (stock, bid, ask, price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

    for q in quotes:
      stock = q['stock']
      bid = float(q['top_bid']['price'])
      ask = float(q['top_ask']['price'])
      price = (bid + ask) / 2

      self.assertEqual(getDataPoint(q), (stock, bid, ask, price))


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453','top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price1 = getDataPoint(quotes[0])[3]
    price2 = getDataPoint(quotes[1])[3]
    self.assertEqual(getRatio(price1, price2), price1 / price2)

  def test_getRatio_calculateInvalidRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price1 = getDataPoint(quotes[0])[3]
    price2 = getDataPoint(quotes[1])[3]

    self.assertEqual(getRatio(price1, 0), 0)
    self.assertEqual(getRatio(0, price2), 0)





if __name__ == '__main__':
    unittest.main()
