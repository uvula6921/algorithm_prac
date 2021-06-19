import sys
num = int(sys.stdin.readline())
paper = []
for _ in range(num):
  paper.append(list(map(int, sys.stdin.readline().split())))
 
blue = 0
white = 0
def cut_paper(width_start, width_finish, height_start, height_finish):
  global blue, white
  first = paper[height_start][width_start]
  for i in range(height_start, height_finish+1):
    for j in range(width_start, width_finish+1):
      if first != paper[i][j]:
        cut_paper(width_start,(width_start+width_finish)//2,height_start,(height_start+height_finish)//2)
        cut_paper((width_start+width_finish)//2+1,width_finish,height_start,(height_start+height_finish)//2)
        cut_paper(width_start,(width_start+width_finish)//2,(height_start+height_finish)//2+1,height_finish)
        cut_paper((width_start+width_finish)//2+1,width_finish,(height_start+height_finish)//2+1,height_finish)
        return
  if first == 1:
    blue += 1
  else:
    white += 1
  return 
    
cut_paper(0,num-1,0,num-1)
print(white)
print(blue)