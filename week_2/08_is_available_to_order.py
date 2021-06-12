shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
  for order in orders:
    if not order in set(menus): 
      # 굳이 집합을 사용하는 이유: 내부적으로 hash를 통해서 자료들을 저장하기 때문에 시간복잡도가 O(1)이 가능하고 해시가 성능이 떨어졌을(충돌이 많은 경우) 때 O(n) 발생.
      return False
  else:
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)