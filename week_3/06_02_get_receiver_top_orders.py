top_heights = [3,9,9,3,5,7,2]

def get_receiver_top_orders(heights):
  result_list = [0] * len(heights)
  for i in range(len(heights)-1):
    h = heights.pop()
    for j in range(len(heights), -1, -1):
      if heights[j-1] > h:
        result_list[-i-1] += j
        break
  return result_list

print(get_receiver_top_orders(top_heights))  # [0, 0, 0, 3, 3, 3, 6] 가 반환되어야 한다!

# O(N^2)