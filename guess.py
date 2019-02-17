import random
r = random.randint(1,100)
print(r)
while True:
    y = input('請猜一個數字')
    y = int(y)
    if y == r:
        print('你猜對囉~')
        break
    else:
        if y > r:
        	print('比答案大，再猜一次')
        else:
        	print('比答案小，再猜一次')