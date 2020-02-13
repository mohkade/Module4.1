def calculate_price():
#def calculate_price(price, cash_coupon, percent_coupon):
#    price = float(input("Input price:"))
#    cash_coupon = float(input("Input cash coupon amount:"))
#    percent_coupon = float(input("Input percent coupon:"))
#    tax = float(round((6/100), 5))
#    new_price = float(round((price - cash_coupon), 5))
#    new_price2 = float(round(new_price / (1 + (percent_coupon / 100)), 5))
#    price2 = int(round(new_price2, 2))
#    final_price = float(round(new_price2 * (1+tax), 5))
#    final = int(round(final_price, 2))
#    return final_price

#try
#cc_discount_price = price - cash_coupon
#if cc_discount_price <= 0:
    #return 0.00

#percent_value = percent_coupon/100

#if percent_value < 0:

#discounted_value = cc_discount_price * (1 - percent_value)

#except TypeError:
 #   print('A typeError occured. Invalid input')
#except:
    #print('something else happened')
#(not needed)finally:


#return discounted_value
#return((price - cash_coupon) * (1 - percent_coupon/100))

   # def price():
    price = int(input("Input price:"))
  #      return price
 #   def cash_coupon():
    cash_coupon = int(input("Input cash coupon amount:"))
#        return cash_coupon
#    def percent_coupon():
    percent_coupon = int(input("Input percent coupon:"))
#        return percent_coupon
    tax = 6/100
    new_price = (price - cash_coupon)
    new_price2 = (new_price / (1 + (percent_coupon / 100)))
#    price2 = int(round(new_price2, 2))
    final_price = new_price2 * (1+tax)
#    final = int(round(final_price, 2))
    return final_price

if __name__ == '__main__':

#    calculate_price()
    ship1 = 5.95
    ship2 = 7.95
    ship3 = 11.95
    ship4 = 0.00
    final_price = float(calculate_price())
    if final_price <= 10.00:
        price1 = (float(round(final_price, 2) + ship1))
        print("Your total is ${} includes shipping cost of ${}".format(price1, ship1))
    elif 10.01 < final_price <= 30.00:
        price2 = (float(round(final_price, 2) + ship2))
        print("Your total is ${} includes shipping cost of ${}".format(price2, ship2))
    elif 30.01< final_price <= 50.00:
        price3 = (float(round(final_price, 2) + ship3))
        print("Your total is ${} includes shipping cost of ${}".format(price3, ship3))
    else:
        price4 = (float(round(final_price, 2)))
        print("Your total is ${} with free shipping!".format(price4))

