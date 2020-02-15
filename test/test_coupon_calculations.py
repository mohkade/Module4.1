import unittest
import unittest.mock as mock
from store import coupon_calculaions as coupon



class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        with mock.patch('builtins.input', side_effects=['7', '5', '10']):
            assert coupon.calculate_new_price2() == 7.88

#below is in class work
        #price: under 10, 5 cash, 10%
#        self.assertEqual(coupon.calculate_price(under_ten, 5, 10),1.8)
        # price: under 10, 5 cash, 15%
  #      self.assertEqual(coupon.calculate_price(under_ten, 5, 15),1.70)
        # price: under 10, 5 cash, 20%
   #     self.assertEqual(coupon.calculate_price(under_ten, 5, 20), 1.60)
        # price: under 10, 5 cash, 25%
    #    self.assertEqual(coupon.calculate_price(under_ten, 5, 25), 1.60)
        # price: under 10, 10 cash, 10%
     #   self.assertEqual(coupon.calculate_price(under_ten, 10, 10), answer)

      #  self.assertEqual(True, False)

#$15.99 - 5.00 = 10.99
#get price of item
#subtract coupon
#discount

if __name__ == '__main__':
    unittest.main()



#def test_set_1(self):
 #   dollar_amt = 7.00
  #  assert coupons.calculate.print(dollar_amt, 5, 10) == 1.80



