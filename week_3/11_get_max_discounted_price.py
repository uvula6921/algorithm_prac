shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):
  dc_prices = []
  for _ in range(len(prices)):
    if len(coupons):
      max_price = max(prices)
      max_coupon = max(coupons)
      dc_price = (max_price * (100-max_coupon))/100
      dc_prices.append(dc_price)
      prices.remove(max_price)
      coupons.remove(max_coupon)
    else:
      dc_prices.append(prices[0])
  
  return sum(dc_prices)

print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.