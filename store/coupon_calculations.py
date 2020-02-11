def calculate_price():
    price = int(input("Input price:"))
    cash_coupon = int(input("Input cash coupon amount:"))
    percent_coupon = int(input("Input percent coupon:"))
    tax = float(round((6/100), 5))
    new_price = float(round((price - cash_coupon), 5))
    new_price2 = float(round(new_price / (1 + (percent_coupon / 100)), 5))
#    price2 = int(round(new_price2, 2))
    final_price = float(round(new_price2 * (1+tax), 5))
#    final = int(round(final_price, 2))
    return final_price
if __name__ == '__main__':

    ship1 = 5.95
    ship2 = 7.95
    ship3 = 11.95
    ship4 = 0.00
    final = int(calculate_price())
    if final <= 10.00:
        print(final+ship1)

